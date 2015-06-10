# -*- coding: utf-8 -*-
import ConfigParser
import os
from tornado.options import define


class Config():
    def __init__(self, file_path):
        config = ConfigParser.ConfigParser()
        path = os.getcwd()
        config.read(path + '/' + file_path)

        sections = config.sections()
        for section in sections:
            options = config.options(section)
            for option in options:
                define(option, default=config.get(section, option))