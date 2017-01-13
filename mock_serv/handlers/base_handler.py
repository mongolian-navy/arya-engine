# -*- coding: utf -*-

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)

