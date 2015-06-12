# -*- coding: utf-8 -*-
import json
import logging
import datetime
import time
import requests

from tornado.options import options


LOG = logging.getLogger(__name__)


class MonitorTask():
    def run(self):
        now = datetime.datetime.now()
        LOG.info('[{0}] start task'.format(now))
        LOG.info('Load api json [{0}]'.format(options.api))
        LOG.info('Load pool json [{0}]'.format(options.pool))

        api_data = open(options.api)
        pool_data = open(options.pool)
        apis = json.load(api_data)
        pools = json.load(pool_data)

        for pool in pools:
            LOG.info('monitor pool [{0}], host [{1}], cos port [{2}], vms port [{3}]'.format(
                pool.get('name'),
                pool.get('host'),
                pool.get('cos_port'),
                pool.get('vms_port'),
            ))
            for api in apis:
                cos_url = "http://{0}:{1}{2}".format(
                    pool.get('host'),
                    pool.get('cos_port'),
                    api.get('cos_api'),
                ).format(pool.get('name'))
                LOG.info('COS url [{0}]'.format(cos_url))
                vms_url = "http://{0}:{1}{2}".format(
                    pool.get('host'),
                    pool.get('vms_port'),
                    api.get('vms_api'),
                )
                LOG.info('VMS url [{0}]'.format(vms_url))

                try:
                    cos_start_time = time.time()
                    cos_request = requests.get(cos_url)
                    cos_end_time = time.time()
                    vms_start_time = time.time()
                    vms_request = requests.get(vms_url)
                    vms_end_time = time.time()

                    LOG.info('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                    LOG.info(cos_request.status_code)
                    LOG.info(vms_request.status_code)
                    cos_cost_time = cos_end_time - cos_start_time
                    vms_cost_time = vms_end_time - vms_start_time
                    LOG.info(cos_cost_time)
                    LOG.info(vms_cost_time)
                    LOG.info('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                except Exception as ex:
                    LOG.error(ex)


def init_data():
    LOG.info('Load data json [{0}]'.format(options.data))
    data_data = open(options.data)
    data = json.load(data_data)
    return data


DATA = init_data()