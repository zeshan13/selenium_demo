#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:41
# @Author  : zeshan
# @File    : add_member_page.py

from selenium_demo.comm.base_page import BasePage
from contact_page import ContactPage

class AddMemberPage(BasePage):
    def add_member(self,username, accid, phone):

        return ContactPage(self.driver)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    # 访问扫码登录页面
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    AddMemberPage(driver)