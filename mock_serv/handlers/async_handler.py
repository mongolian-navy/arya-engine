# -*- coding: utf-8 -*-

import requests

import tornado.web
import tornado.gen

from base_handler import BaseHandler

class AsyncHandler(BaseHandler):

    def __init__(self, *args, **kwargs):
        super(AsyncHandler, self).__init__(*args, **kwargs)

    @tornado.gen.coroutine
    def block_operation(self, method, url):
        response = requests.request(method, url)
        return response.content

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        response = yield tornado.gen.Task(self.block_operation, "GET", "http://www.hao123.com")
        self.write(response)
        self.finish()