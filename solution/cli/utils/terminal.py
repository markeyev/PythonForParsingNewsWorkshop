import datetime
from collections import Counter

from models.functions import is_post_stared, db
from settings import CURRENT_PROJECT
from utils.kbhit import KBHit


def prompt(*, text: str, y_n=True, kb=None) -> bool:
    print(text + ' [pres y or n]')

    if kb is None:
        kb = KBHit()

    if y_n is True:
        while True:
            if kb.hit():
                c = kb.get_char()
                if c in 'yYnN':
                    break
        return bool(c in 'yY')
    return False


def clear_term() -> None:
    print(chr(27) + "[2J")
    print(chr(27) + "[1;1f")
    print(f'Current project: {CURRENT_PROJECT}.')
    print('-' * 40)


def echo(text: str) -> None:
    print(text)


def show_post(post: dict) -> None:
    clear_term()
    try:
        stared = '*' if is_post_stared(post['_id']) else ''
        print(f'''{datetime.datetime.fromtimestamp(post['published'])} {stared} 
{post["title"]}

{post["url"]}

{post["summary"]}

{post["content"]}

{', '.join(post["tags"])}
---------------------------------
j - next, r - remove, ESC - exit.

''')
    except TypeError:
        print('No more posts.')


def print_stats():
    print(f'feeds    = {db.feeds.count_documents({})}, \n'
          f'posts    = {db.posts.count_documents({})}, \n'
          f'stared   = {db.stared.count_documents({})}, \n')

    for feed in db.feeds.find({}):
        print(f'''{feed['_id']} - {feed['url']}''')
