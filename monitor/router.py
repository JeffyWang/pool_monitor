# -*- coding: utf-8 -*-
from monitor.handler.main import MainHandler


router = [
    (r"/", MainHandler),
]