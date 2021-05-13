import logging
import time

from pymongo import errors

from models.functions import db
from remote_services.feedparser_grpc_api_client import get_feed_posts_from_api

REPLACE = '---'


def sync_catalog_from_file():
    """We're expecting next file structure:
        <beginning of file>https://some-rss-feed-url.xml\n
https://another-rss-feed-url.xml<end of file>

    :return:
    """
    db.feeds.drop()
    db.posts.drop()
    with open('catalog.txt', 'r') as f:
        data = f.read().split('\n')
        for feed in data:
            if feed:
                db.feeds.insert_one({
                    'url': feed,
                    'etag': '',
                    'modified': 0,
                    'interval': 30
                })


def parse_feeds_from_mongo():
    for feed in db.feeds.find({}):

        if (feed['modified'] and
                time.time() < feed['modified'] + feed['interval']):
            logging.info(f'''{feed['url']=} skipped, because {time.time()=} < '''
                         f'''{feed['modified'] + feed['interval']}''')
            continue

        logging.info(f'''Start parsing {feed['url']=}.''')

        try:
            parsed_feed = get_feed_posts_from_api(feed_url=feed['url'],
                                                  modified=feed['modified'],
                                                  etag=feed['etag'],
                                                  interval=feed['interval'])
        except TimeoutError:
            logging.error(f'''Parsing timeout for {feed}.''')
            return

        for parsed_post in parsed_feed.posts:
            logging.info(f'{parsed_post=}')

            if (not parsed_post.summary or parsed_post.summary == 'None' or
                    len(parsed_post.title) + len(parsed_post.summary) < 60):
                continue

            try:
                result = db.posts.insert_one(
                    dict(
                        url=parsed_post.url,
                        feed=feed['_id'],
                        published=parsed_post.published,
                        title=parsed_post.title,
                        summary=parsed_post.summary,
                        content=parsed_post.content,
                        tags=list(map(str, parsed_post.tags))
                    )
                )
                logging.info(f'{result.inserted_id=} {parsed_post.title=}')
            except errors.DuplicateKeyError:
                logging.error(f'Duplicate {parsed_post.url=}')

        db.feeds.replace_one({'_id': feed['_id']}, {
            'url': feed['url'],
            'etag': parsed_feed.etag,
            'modified': parsed_feed.modified,
            'interval': parsed_feed.interval
        })
        logging.info(f'''{feed['url']=} parsed and updated with {feed=}''')
