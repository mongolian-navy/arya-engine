# -*- coding: utf -*-

from base_handler import BaseHandler


class DispatchHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("index.html")

    def post(self, *args, **kwargs):
        print self.request.params
        self.write("200")
        self.finish()
