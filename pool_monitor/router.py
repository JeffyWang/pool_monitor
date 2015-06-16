# -*- coding: utf-8 -*-
from pool_monitor.handler.main import MainHandler
from pool_monitor.handler.monitor import MonitorHandler


router = [
    (r"/", MainHandler),
    (r"/monitor", MonitorHandler),
]