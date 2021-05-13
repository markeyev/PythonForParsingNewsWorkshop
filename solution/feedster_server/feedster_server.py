#!/usr/bin/python3

import logging
import os
from concurrent import futures
from typing import Text

import grpc
from feedparser_wrapper.feedparser_wrapper import Feed, NotChanged

import feedster_pb2
import feedster_pb2_grpc

_PORT = os.environ["PORT"]


class Parser(feedster_pb2_grpc.ParserServicer):

    def Download(self, request, context):
        feed_url = request.url

        feed = feedster_pb2.FeedParsingResponse(
            url=feed_url,
            modified=request.modified,
            etag=request.etag or '',
            interval=request.interval
        )

        try:
            output = Feed(feed_url=feed_url, modified=request.modified,
                          etag=request.etag).parse()
        except NotChanged:
            return feed

        feed.modified = output['modified'] or request.modified
        feed.etag = output['etag'] or ''
        feed.interval = output['interval'] or request.interval

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


def _serve(port: Text):
    bind_address = f"[::]:{port}"
    server = grpc.server(futures.ThreadPoolExecutor())
    feedster_pb2_grpc.add_ParserServicer_to_server(Parser(), server)
    server.add_insecure_port(bind_address)
    server.start()
    logging.info("Listening on %s.", bind_address)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    _serve(_PORT)
