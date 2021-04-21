#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:41
# @Author  : zeshan
# @File    : contact_page.py
import time

from selenium_demo.comm.base_page import BasePage
from add_member_page import AddMemberPage
from selenium.webdriver.common.by import By

class ContactPage(BasePage):
    _username = (By.CSS_SELECTOR, "[id='username']")
    _accid = (By.CSS_SELECTOR, "[id='memberAdd_acctid']")
    _email  = (By.CSS_SELECTOR, "[id='memberAdd_mail']")
    _save_btn = (By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save")

    def get_contact_list(self):
        contact_list = []
        return contact_list


    def goto_add_member(self):
        # 调用js点击"添加员工"按钮
        time.sleep(5)
        self.execute_script("document.getElementsByClassName('qui_btn ww_btn js_add_member')[0].click()")
        return AddMemberPage(self.driver)