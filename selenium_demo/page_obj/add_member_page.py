#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:41
# @Author  : zeshan
# @File    : add_member_page.py

from selenium_demo.comm.base_page import BasePage
from contact_page import ContactPage
from selenium.webdriver.common.by import By

class AddMemberPage(BasePage):
    _username = (By.CSS_SELECTOR, "[id='username']")
    _accid = (By.CSS_SELECTOR, "[id='memberAdd_acctid']")
    _email  = (By.CSS_SELECTOR, "[id='memberAdd_mail']")
    _save_btn = (By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save")

    def add_member(self,username, accid, email):
        # 输入员工名称
        self.find_element(self._username).send_keys(username)
        # 输入工号
        self.find_element(self._accid).send_keys(accid)
        # 输入邮箱
        self.find_element(self._email).send_keys(email)
        # 点击保存按钮
        self.find_element(self._save_btn).click()
        return ContactPage(self.driver)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    # 访问扫码登录页面
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    AddMemberPage(driver)