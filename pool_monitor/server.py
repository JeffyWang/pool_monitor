# -*- coding: utf-8 -*-
import json
import logging
import logging.config
from os.path import join
from tornado.options import options
import tornado.ioloop
import tornado.web
import tornado.httpserver
from conf.conf import Config
from pool_monitor.router import router
from pool_monitor.task.monitor import MonitorTask
from pool_monitor.context import context


LOG = logging.getLogger(__name__)


class Application(tornado.web.Application):
    def __init__(self, config):
        handler = router
        LOG.info('Staitc path is [{0}]'.format(join(config.PROJECT_DIR, 'static')))
        setting = {
            'template_path': join(config.PROJECT_DIR, 'templates'),
            'static_path': join(config.PROJECT_DIR, 'static'),
            'debug': True
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

    init_data()
    period = 10 * 60 * 1000
    tornado.ioloop.PeriodicCallback(init_task, period).start()
    tornado.ioloop.IOLoop.instance().start()


def init_task():
    monitor = MonitorTask()
    monitor.run()


def init_config():
    options.parse_command_line()
    config = Config('monitor.conf')
    return config


def init_data():
    LOG.info('Load data json [{0}]'.format(options.data))
    data_data = open(options.data)
    data = json.load(data_data)
    context.DATA = data


def main():
    run_server()