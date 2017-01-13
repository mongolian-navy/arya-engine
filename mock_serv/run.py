# -*- coding: utf-8 -*-

import tornado.options

from app.server import Server
from app.application import Application

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application()
    server = Server(app)
    server.run_server()