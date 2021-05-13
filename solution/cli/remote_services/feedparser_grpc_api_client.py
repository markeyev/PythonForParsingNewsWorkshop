import logging

import grpc

from remote_services import feedster_pb2, feedster_pb2_grpc
from settings import GRPC_PARSING_API_URL, PARSING_TIMEOUT


def get_feed_posts_from_api(*, feed_url: str,
                            etag: str = None,
                            modified: int = None,
                            interval: int = 0) -> dict:

    with grpc.insecure_channel(GRPC_PARSING_API_URL) as channel:

        stub = feedster_pb2_grpc.ParserStub(channel)
        try:
            response = stub.Download(
                feedster_pb2.FeedParsingRequest(
                    url=feed_url,
                    etag=etag,
                    modified=modified,
                    interval=interval,
                ), timeout=PARSING_TIMEOUT
            )
            return response
        except Exception as e:
            logging.error('%s for %s.', e, feed_url)
