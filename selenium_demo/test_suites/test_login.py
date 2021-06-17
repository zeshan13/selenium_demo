#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:49
# @Author  : zeshan
# @File    : test_login.py
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium_demo.comm import config
from selenium_demo.comm.do_yaml import DoYaml
cfg = config.COMMCFG

@pytest.mark.skip()
@pytest.mark.first
class TestLogin():
    def test_login(self,driver):
        time.sleep(5) #第一次登录等待扫码
        cookies  = driver.get_cookies()
        # 存储首次登录cookies
        DoYaml().write_yaml(file_path=cfg.COOKIES_PATH, content=cookies)
        WebDriverWait(driver, 30).until(EC.url_to_be(cfg.MAIN_URL))
