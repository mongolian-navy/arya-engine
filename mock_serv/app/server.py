# -*- coding: utf-8 -*-

from tornado.httpserver import HTTPServer
from tornado.options import options
import tornado.ioloop

from utils.log import LOG
from timer_task import TimerTask

class Server(HTTPServer):

    def __init__(self, app):
        super(Server, self).__init__(app)

    def run_server(self):
        LOG.info("Server is listening port: %d" % options.port)
        self.listen(options.port)
        timer_task = TimerTask(self)
        timer_task.start()
        try:
            LOG.info("Server is running now!")
            tornado.ioloop.IOLoop.instance().start()
        except KeyboardInterrupt:
            LOG.info("Server closed.")
            tornado.ioloop.IOLoop.instance().stop()