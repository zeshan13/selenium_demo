#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-19 21:30
# @Author  : zeshan
# @File    : run.py
import os
from comm import config
cfg = config.COMMCFG
if __name__ == '__main__':
    result = cfg.result_dir
    report = cfg.report_dir
    os.system("python -m pytest")
    os.system("allure generate --clean "+result+"  --report-dir "+report)
