import logging

from bson import ObjectId, BSONOBJ
from pymongo import (errors, MongoClient, ASCENDING)

from settings import PROJECTS, CURRENT_PROJECT


def get_db():
    client = MongoClient(*PROJECTS[CURRENT_PROJECT]['MONGODB_CONN'])
    return getattr(client, PROJECTS[CURRENT_PROJECT]['MONGODB_DBNAME'])


db = get_db()

db.feeds.create_index([('url', ASCENDING)], unique=True)
db.posts.create_index([('url', ASCENDING)], unique=True)
db.stared.create_index([('post', ASCENDING)], unique=True)


class BadParams(Exception):
    pass


def remove_post(oid: ObjectId) -> None:
    if is_post_stared(oid):
        switch_post_star(_id=oid)
    logging.info(db.posts.delete_one({'_id': oid}))


def is_post_stared(oid: ObjectId) -> bool:
    try:
        return bool(db.stared.find_one({'post': oid})['_id'])
    except TypeError:
        return False


def add_feed_to_mongo(*, url: str) -> ObjectId:
    try:
        response = db.feeds.insert_one({
            'url': url,
            'etag': '',
            'modified': 0,
            'interval': 0
        })
        return response.inserted_id
    except errors.DuplicateKeyError:
        logging.error(f'{url=} already in DB.')


def switch_post_star(*, _id: ObjectId) -> None:
    try:
        db.stared.insert_one({
            'post': _id,
        })
    except errors.DuplicateKeyError:
        db.stared.find_one_and_delete({
            'post': _id,
        })


def get_post(*, search_dict: dict = None,
             oid: ObjectId = None,
             sort: list = None) -> BSONOBJ:
    if sort is None:
        sort = [("_id", ASCENDING)]

    if search_dict:
        return db.posts.find_one(search_dict, sort=sort)

    return db.posts.find_one({'post': oid}, sort=sort)
