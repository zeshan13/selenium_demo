#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:49
# @Author  : zeshan
# @File    : test_add_member.py
import time
import pytest
from selenium_demo.comm import config
from selenium_demo.comm.do_yaml import DoYaml
cfg = config.COMMCFG


class TestAddMember():
    @pytest.mark.skip()
    @pytest.mark.first
    def test_login(self,driver):
        time.sleep(3) #第一次登录等待扫码
        cookies  = driver.get_cookies()
        # 存储首次登录cookies
        DoYaml().write_yaml(file_path=cfg.cookies_path, content=cookies)

    @pytest.mark.parametrize("username, accid, email",[["小黄6", "0066", "12345678965@qq.com"]])
    def test_add_member_in_contact_page(self,username, accid, email,main_page):
        contact_list = main_page.goto_contact_page().goto_add_member().add_member(username, accid, email).get_contact_list()
        assert username in contact_list

    @pytest.mark.parametrize("username, accid, email", [["小黑6", "065", "98765432126@qq.com"]])
    def test_add_member_in_main_page(self,username, accid, email,main_page):
        contact_list = main_page.goto_add_member().add_member(username, accid, email).get_contact_list()
        assert username in contact_list


    def test_add_member_continue(self,main_page):
        members_dic_list = [{"username":"小黑122","accid":"0222","email":"1234215@qq.com"},
                            {"username":"小黑123","accid":"0324","email":"126271@qq.com"}]
        contact_list = main_page.goto_add_member().add_member_continue(*members_dic_list).get_contact_list()
        assert members_dic_list[0]["username"] in contact_list
        assert members_dic_list[1]["username"] in contact_list