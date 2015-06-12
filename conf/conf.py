# -*- coding: utf-8 -*-
import ConfigParser
from os.path import abspath, dirname, join
from tornado.options import define


class Config():
    CONF_DIR = dirname(abspath(__file__))
    PROJECT_DIR = dirname(CONF_DIR)

    def __init__(self, file_name):
        config = ConfigParser.ConfigParser()
        config.read(join(self.CONF_DIR, file_name))

        define('api', join(self.CONF_DIR, 'api.json'))
        define('pool', join(self.CONF_DIR, 'pool.json'))
        define('data', join(self.CONF_DIR, 'data.json'))

        sections = config.sections()
        for section in sections:
            options = config.options(section)
            for option in options:
                define(option, default=config.get(section, option))