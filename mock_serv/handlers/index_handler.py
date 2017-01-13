# -*- coding: utf -*-

from tornado.web import RequestHandler
from base_handler import BaseHandler


class IndexHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("index.html")

    def post(self, *args, **kwargs):
        print self.request.params
        self.write("200")
        self.finish()
