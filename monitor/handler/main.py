# -*- coding: utf-8 -*-
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        data = dict(
            a=1,
            b='2'
        )
        self.write(data)