#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-19 21:30
# @Author  : zeshan
# @File    : run.py
import os
from comm import config

CFG = config.COMMCFG
if __name__ == '__main__':
    result = CFG.RESULT_DIR
    report = CFG.REPORT_DIR
    os.system("python -m pytest")
    os.system("allure generate --clean " + result + "  --report-dir " + report)
