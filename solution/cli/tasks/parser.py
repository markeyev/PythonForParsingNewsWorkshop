import logging

from feedparser_wrapper.exceptions import NotChanged
from feedparser_wrapper.feedparser_wrapper import Feed

from remote_services import feedster_pb2


def parse(*, url: str, modified: int, interval: int, etag: str = ''):
    feed_url = url

    try:
        output = Feed(feed_url=feed_url, modified=modified, etag=etag).parse()
    except NotChanged:
        return {

        }

    modified = output['modified'] or modified
    etag = output['etag'] or ''
    interval = output['interval'] or interval

    feed = dict(feed_url=url, modified=modified, etag=etag, interval=interval,
                posts=[])

    posts = []
    for item in output.get('posts'):
        logging.debug(item)

        post = feedster_pb2.Post(**item)
        if 'tags' in item:
            post.tags.extend(item['tags'])
        else:
            post.tags.extend([])
        posts.append(post)

    if posts:
        feed.posts.extend(posts)

    return feed
