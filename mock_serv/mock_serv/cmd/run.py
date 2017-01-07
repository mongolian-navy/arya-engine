# -*- coding: utf-8 -*-
#


import os
import sys

# If ../__init__.py exists, add ../ to Python search path, so that
# it will override what happens to be installed in /usr/(local/)lib/python...
possible_topdir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                   os.pardir,
                                    os.pardir,
                                    os.pardir))
if os.path.exists(os.path.join(possible_topdir, 'mock_serv', '__init__.py')):
        sys.path.insert(0, possible_topdir)


import mock_serv.util.config
from mock_serv.util import log as logging
from mock_serv import http_server
import mock_serv.timer_task

def prepare():
    task = mock_serv.timer_task.TimerTask()
    task.start()

def main():
    mock_serv.util.config.init_options()
    log_list = ('Main','Access')

    server = http_server.Server(http_server.TApplication('mock_serv'), prepare, log_list)
    server.start()

if __name__ == '__main__':
    main()
