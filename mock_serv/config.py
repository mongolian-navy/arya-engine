# -*- coding: utf-8 -*-

import os
from tornado.options import options, define
from handlers.dispatch_handler import DispatchHandler

define("env", default="debug", help="service run environment")
define("port", default=8080, type=int, help="bind port")

STATIC_PATH = os.path.join(os.path.dirname(__file__), 'static')
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates')

APP_SETTINGS = {
    'gzip': 'on',
    'static_path': STATIC_PATH,
    'template_path': TEMPLATE_PATH,
    'debug': options.env == "debug",
    'default_handler_class': DispatchHandler,
}
