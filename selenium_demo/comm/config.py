#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-19 21:31
# @Author  : zeshan
# @File    : config.py
import os

class ConstError(Exception): pass

class _const(object):
    def __setattr__(self, k, v):
        if k in self.__dict__:
            raise ConstError
        else:
            self.__dict__[k] = v


COMMCFG = _const()
COMMCFG.LOGIN_URL = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome"
COMMCFG.MAIN_URL = "https://work.weixin.qq.com/wework_admin/frame"

COMMCFG.BASE_DIR = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
COMMCFG.COMM_DIR = os.path.join(COMMCFG.BASE_DIR, "comm")
COMMCFG.TOOLS_DIR = os.path.join(COMMCFG.BASE_DIR, "tools")
COMMCFG.REPORT_DIR = os.path.join(COMMCFG.BASE_DIR, "report")
COMMCFG.LOGS_DIR = os.path.join(COMMCFG.BASE_DIR, "logs")
COMMCFG.RESULT_DIR = os.path.join(COMMCFG.BASE_DIR, "result")
COMMCFG.SCREENSHOTS_DIR = os.path.join(COMMCFG.BASE_DIR, "screenshots")
COMMCFG.TEST_DATAS_DIR = os.path.join(COMMCFG.BASE_DIR, "test_datas")
COMMCFG.COOKIES_PATH = os.path.join(COMMCFG.COMM_DIR, "cookies.yaml")
COMMCFG.INIT_DATAS_PATH = os.path.join(COMMCFG.TEST_DATAS_DIR, "init_datas.yaml")
COMMCFG.CHROMEDRIVER_PATH = os.path.join(COMMCFG.TOOLS_DIR, "chromedriver.exe")
COMMCFG.CHROMEDRIVER_FOR_MAC_PATH = os.path.join(COMMCFG.TOOLS_DIR, "chromedriver")



if __name__ == '__main__':
    print(COMMCFG.BASE_DIR)
    print(COMMCFG.COOKIES_PATH)
