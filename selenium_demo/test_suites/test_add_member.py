#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:49
# @Author  : zeshan
# @File    : test_add_member.py
import time

from selenium_demo.page_obj.main_page import MainPage
from selenium_demo.page_obj.contact_page import ContactPage
from selenium_demo.page_obj.add_member_page import AddMemberPage
from selenium import webdriver
from selenium_demo.comm import config
from selenium_demo.comm.do_yaml import DoYaml


cfg = config.COMMCFG
do_yaml = DoYaml()

class TestAddMember():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url=cfg.login_url)
        self.driver.maximize_window()
        time.sleep(3)
        cookies = self.driver.get_cookies()
        do_yaml.write_yaml(file_path=cfg.cookies_path,content=cookies)
        # cookies = do_yaml.read_yaml(file_path=cfg.cookies_path)
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        self.driver.get(url=cfg.main_url)

        self.main_page = MainPage(self.driver)

    def teardown(self):
        self.driver.quit()


    def test_add_member_in_contact_page(self):
        username = "小黄1"
        accid = "142"
        email = "123456781@qq.com"
        contact_list = self.main_page.goto_contact_page().goto_add_member().add_member(username, accid, email).get_contact_list()
        assert username in contact_list

    def test_add_member_in_main_page(self,):
        username = "小黑1"
        accid = "112"
        email = "123456783@qq.com"
        contact_list = self.main_page.goto_add_member().add_member(username, accid, email).get_contact_list()
        assert username in contact_list

if __name__ == '__main__':
    pass



