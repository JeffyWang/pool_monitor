# -*- coding: utf-8 -*-
from tornado.options import options
import tornado.ioloop
import tornado.web
import tornado.httpserver
from conf.conf import Config
from monitor.router import router


class Application(tornado.web.Application):
    def __init__(self):

        handler = router
        setting = {

        }
        tornado.web.Application.__init__(self, handler, **setting)


def run_server():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


def init_config():
    options.parse_command_line()
    Config('conf/monitor.conf')


def main():
    init_config()
    run_server()