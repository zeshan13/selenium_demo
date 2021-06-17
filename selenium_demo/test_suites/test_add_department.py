#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-24 16:37
# @Author  : zeshan
# @File    : test_add_department.py
import time

import pytest
from selenium_demo.comm import config
from selenium_demo.comm.do_yaml import DoYaml
cfg = config.COMMCFG


class TestAddDepartment():
    @pytest.mark.skip()
    @pytest.mark.first
    def test_login(self,driver):
        time.sleep(3) #第一次登录等待扫码
        cookies  = driver.get_cookies()
        # 存储首次登录cookies
        DoYaml().write_yaml(file_path=cfg.COOKIES_PATH, content=cookies)

    @pytest.mark.parametrize("name",["财务部",])
    def test_add_department_in_contact_page(self,name,main_page):
        department_list = main_page.goto_contact_page().goto_add_department().add_department(name).get_department_list()
        assert name in department_list
