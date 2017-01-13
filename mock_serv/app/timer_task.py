# -*- coding: utf-8 -*-

import tornado.ioloop
from utils.log import LOG


class TimerTask(object):
    def __init__(self, server):
        self.server = server
        def _task_func():
            LOG.info("Timer task run.")
        self._task_func = tornado.ioloop.PeriodicCallback(_task_func, 20*1000)

    def start(self):
        self._task_func.start()

    def stop(self):
        self._task_func.stop()