#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-24 16:37
# @Author  : zeshan
# @File    : test_imoort_contacts.py
import os
import time

import pytest
from selenium_demo.comm import config
from selenium_demo.comm.do_yaml import DoYaml
cfg = config.COMMCFG


class TestImportContacts():
    @pytest.mark.skip()
    @pytest.mark.first
    def test_login(self,driver):
        time.sleep(3) #第一次登录等待扫码
        cookies  = driver.get_cookies()
        # 存储首次登录cookies
        DoYaml().write_yaml(file_path=cfg.cookies_path, content=cookies)

    def test_import_contacts_in_contact_page(self,main_page):
        file_path = os.path.join(cfg.test_datas_dir,"import_contacts_sanzhang.xlsx")
        contact_list = main_page.goto_contact_page().goto_import_contacts_by_file().import_contact_by_file(file_path).get_contact_list()
        assert "张三（示例）" in contact_list

    def test_import_contacts_in_main_page(self,main_page):
        file_path = os.path.join(cfg.test_datas_dir, "import_contacts_sili.xlsx")
        contact_list = main_page.goto_import_contacts_by_file().import_contact_by_file(file_path).get_contact_list()
        assert "李四（示例）" in contact_list
