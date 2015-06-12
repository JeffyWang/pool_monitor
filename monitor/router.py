# -*- coding: utf-8 -*-
from monitor.handler.main import MainHandler
from monitor.handler.monitor import MonitorHandler


router = [
    (r"/", MainHandler),
    (r"/monitor", MonitorHandler),
]