#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-17 2:13
# @Author  : zeshan
# @File    : run.py
import os

if __name__ == '__main__':
    # os.system("python -m pytest")
    os.system("allure generate --clean ./result  --report-dir ./report")


