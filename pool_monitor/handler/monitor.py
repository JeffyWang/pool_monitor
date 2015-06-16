# -*- coding: utf-8 -*-
import json
import logging
from tornado.options import options
import tornado.web
import tornado.gen
from pool_monitor.context import context

LOG = logging.getLogger(__name__)


class MonitorHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):

        self.write(json.dumps(context.DATA))