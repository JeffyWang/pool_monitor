# -*- coding: utf-8 -*-
import logging
import logging.config
from os.path import join
from tornado.options import options
import tornado.ioloop
import tornado.web
import tornado.httpserver
from conf.conf import Config
from monitor.router import router


LOG = logging.getLogger(__name__)


class Application(tornado.web.Application):
    def __init__(self, config):
        handler = router
        LOG.info('Staitc path is [{0}]'.format(join(config.PROJECT_DIR, 'static')))
        setting = {
            'template_path': join(config.PROJECT_DIR, 'templates'),
            'static_path': join(config.PROJECT_DIR, 'static'),
        }
        tornado.web.Application.__init__(self, handler, **setting)


def run_server():
    config = init_config()
    logging.config.fileConfig(join(config.CONF_DIR, 'log.conf'))

    http_server = tornado.httpserver.HTTPServer(Application(config))
    http_server.listen(options.port)
    LOG.info('Staring server with port [{0}], conf [{1}]'.format(
        str(options.port), join(config.CONF_DIR, 'log.conf')
    ))
    tornado.ioloop.IOLoop.instance().start()


def init_config():
    options.parse_command_line()
    config = Config('monitor.conf')
    return config


def main():
    run_server()