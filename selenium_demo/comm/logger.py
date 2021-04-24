#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-21 0:02
# @Author  : zeshan
# @File    : logger.py
import logging
import os
import time
from selenium_demo.comm import config
cfg = config.COMMCFG

class Logger(object):

    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        log_name = os.path.join(cfg.logs_dir ,rq + '.log')
        fh = logging.FileHandler(log_name,encoding="utf-8")
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getLog(self):
        return self.logger

if __name__ == '__main__':
    print(cfg.logs_dir)
