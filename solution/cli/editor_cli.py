import argparse
import logging
import subprocess

from bson import BSONOBJ
from pymongo import ASCENDING, DESCENDING

from controllers import parse_feeds_from_mongo, sync_catalog_from_file
from models.functions import (remove_post, is_post_stared, switch_post_star,
                              get_post, add_feed_to_mongo)
from utils.kbhit import KBHit
from utils.terminal import (prompt, clear_term, echo, show_post, print_stats)


class PostIter:
    FORWARD = 'F'
    BACKWARD = 'B'

    def __init__(self) -> None:
        self._sort = [("published", ASCENDING), ("_id", ASCENDING)]
        self._rsort = [("published", DESCENDING), ("_id", ASCENDING)]
        self._post = get_post(search_dict={}, sort=self._sort)
        self.direction = PostIter.FORWARD

    def current(self) -> BSONOBJ:
        return self._post

    def next(self) -> BSONOBJ:
        if self._post is None:
            self._post = get_post(search_dict={}, sort=self._sort)
        else:
            self._post = get_post(
                search_dict={'published': {'$gt': self._post['published']}},
                sort=self._sort
            )
        self.direction = PostIter.FORWARD
        return self._post

    def prev(self) -> BSONOBJ:
        if self._post is None:
            self._post = get_post(search_dict={}, sort=self._rsort)
        else:
            self._post = get_post(
                search_dict={'published': {'$lt': self._post['published']}},
                sort=self._rsort)
        self.direction = PostIter.BACKWARD
        return self._post

    def next_by_direction(self) -> BSONOBJ:
        if self.direction == PostIter.FORWARD:
            return self.next()
        else:
            return self.prev()


def cli():
    kb = KBHit()

    posts = PostIter()
    post = posts.current()
    show_post(post)

    while True:

        if kb.hit():

            c = kb.get_char()

            if ord(c) == 27 or c == 'q':  # ESC or q
                break

            elif c == 'c':  # Redraw current post.
                show_post(post)

            elif c == 'r':  # Remove current post.
                show_post(post)
                if is_post_stared(post['_id']):

                    res = prompt(text='Are you sure?', kb=kb)

                    if res:
                        remove_post(post['_id'])
                        post = posts.next_by_direction()
                        show_post(post)
                else:
                    remove_post(post['_id'])
                    post = posts.next_by_direction()
                    show_post(post)

            elif c == 'j':  # Go to next post (forward).
                post = posts.next()
                show_post(post)

            elif c == 'k':  # Go to prev post (backward).
                post = posts.prev()
                show_post(post)

            elif c == 'v':  # Open post url in browser.
                subprocess.call(['open', post['url']])

            elif c == 's':  # Add star to post (make post stared).
                switch_post_star(_id=post['_id'])
                show_post(post)

            elif c == 'i':  # Show statistics.
                clear_term()
                print_stats()

            elif c == 'p':  # Run parsing.
                clear_term()
                echo('Parsing...')
                parse_feeds_from_mongo()
                echo('Parsing done.')

            elif c == 'a':  # Add feed to db.
                feed_url = input('Paste feed URL: ')
                oid = add_feed_to_mongo(url=feed_url)
                echo(f'Feed {feed_url} added {oid}.')

            elif c == 'b':
                clear_term()
                echo('Getting feeds from file...')
                sync_catalog_from_file()

            else:
                print(f'Keyboard was hit with char = {c} and it means nothing.')

    kb.set_normal_term()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action='count', default=0)
    args = parser.parse_args()  # ['-vvv']

    if args.verbose == 0:
        level = logging.ERROR
    elif args.verbose == 1:
        level = logging.WARNING
    elif args.verbose == 2:
        level = logging.INFO
    else:
        level = logging.ERROR

    logging.basicConfig(level=level)

    cli()
