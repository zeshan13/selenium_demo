#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:40
# @Author  : zeshan
# @File    : main_page.py
from selenium_demo.comm.base_page import BasePage
from add_member_page import AddMemberPage
from contact_page import ContactPage

class MainPage(BasePage):
    def add_member(self,username, accid, phone):

        return AddMemberPage(self.driver)


    def goto_contact_page(self):

        return ContactPage(self.dirver)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    # 访问扫码登录页面
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    MainPage(driver).goto_contact_page()