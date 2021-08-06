#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:41
# @Author  : zeshan
# @File    : add_member_page.py
from selenium.webdriver.common.by import By


class AddMemberPageEle:
    _username = (By.CSS_SELECTOR, "[id='username']")
    _accid = (By.CSS_SELECTOR, "[id='memberAdd_acctid']")
    _email = (By.CSS_SELECTOR, "[id='memberAdd_mail']")
    _save_btn = (By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save")
    _save_and_continue_btn = (By.CSS_SELECTOR, "a.qui_btn.ww_btn.ww_btn_Blue.js_btn_continue")
    _save_succ_tip = (By.CSS_SELECTOR, "#js_tips")
