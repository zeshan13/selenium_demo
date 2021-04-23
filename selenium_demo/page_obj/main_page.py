#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:40
# @Author  : zeshan
# @File    : main_page.py
import time

from selenium_demo.comm.base_page import BasePage
from selenium_demo.page_obj.add_member_page import AddMemberPage
from selenium_demo.page_obj.contact_page import ContactPage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    _add_member_btn = (By.CSS_SELECTOR, "[node-type='addmember']")
    _menu_contacts_locator = (By.CSS_SELECTOR, "[id='menu_contacts']")
    def goto_add_member(self,):
        # 点击添加员工
        self.find_element(self._add_member_btn).click()
        return AddMemberPage(self.driver)

    def goto_contact_page(self):
        time.sleep(7)
        self.find_element(self._menu_contacts_locator).click()
        return ContactPage(self.driver)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    # 访问扫码登录页面
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    MainPage(driver).goto_contact_page()
