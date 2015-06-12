# -*- coding: utf-8 -*-
import logging
import tornado.web
import tornado.gen


LOG = logging.getLogger(__name__)


class MainHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        self.render('index.html')
