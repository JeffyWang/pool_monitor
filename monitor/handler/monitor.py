# -*- coding: utf-8 -*-
import json
import logging
from tornado.options import options
import tornado.web
import tornado.gen


LOG = logging.getLogger(__name__)


class MonitorHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):

        try:
            LOG.info('Load data json [{0}]'.format(options.data))
            data_data = open(options.data)
            data = json.load(data_data)

        except Exception as ex:
            LOG.error(ex)

        self.write(json.dumps(data))