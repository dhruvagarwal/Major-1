# custom mq module
# use rq for redis as mq
import json

from redis import Redis
from rq import Queue


class Producer(object):
    def __init__(self, conn_url="http://localhost", port="1234"):
        self.conn_url = conn_url
        self.port = port

        redis_conn = Redis() # add conn_url here
        self.q = Queue(connection=redis_conn)

    def push(self, message):
        # we assume message is a string

        if not isinstance(message, str):
            raise Exception("Pass only string to the Producer")

        self.q.enqueue(message)

