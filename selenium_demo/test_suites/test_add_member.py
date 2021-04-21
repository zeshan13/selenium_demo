#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:49
# @Author  : zeshan
# @File    : test_add_member.py
from selenium_demo.page_obj.main_page import MainPage
from selenium_demo.page_obj.contact_page import ContactPage
from selenium_demo.page_obj.add_member_page import AddMemberPage
from selenium import webdriver

class TestAddMember():

    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url="https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        self.main_page = MainPage(self.driver)

    def test_add_member_in_contact_page(self):
        username = "小黄"
        accid = "111"
        email = "123456789@qq.com"
        contact_list = self.main_page.goto_contact_page().goto_add_member().add_member(username, accid, email).goto_contact_list()

    def test_add_member_in_main_page(self,):
        username = "小黄"
        accid = "111"
        email = "123456789@qq.com"
        contact_list = self.main_page.goto_add_member().add_member(username, accid, email).goto_contact_list()




