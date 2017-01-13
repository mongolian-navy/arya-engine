# -* coding: utf -*-

import index_handler
import async_handler

ROUTES = [(r'/', index_handler.IndexHandler),
          (r'/async', async_handler.AsyncHandler),]
