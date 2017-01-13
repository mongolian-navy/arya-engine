# -*- coding: utf-8 -*-

import tornado.web

from config import APP_SETTINGS
from handlers import ROUTES
from utils.log import LOG
from lib.url_trie_tree import PathTrie 

class Application(tornado.web.Application):

    def _init_url_tree(self):
        pass

    def __init__(self):
        LOG.info("Server application initializing.")
        LOG.info("App debug switch : %s" % APP_SETTINGS['debug'])
        super(Application, self).__init__(ROUTES, **APP_SETTINGS)
        self.url_tree = PathTrie()
        LOG.info("Server application initialization done.")
