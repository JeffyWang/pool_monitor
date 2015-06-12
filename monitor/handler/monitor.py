# -*- coding: utf-8 -*-
import logging
import tornado.web


LOG = logging.getLogger(__name__)


class MonitorHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):

        try:
            data = {
                'a': 1
            }
        except Exception as ex:
            LOG.error(ex)

        self.write(data)