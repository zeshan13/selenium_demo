#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:40
# @Author  : zeshan
# @File    : main_page.py

from selenium.webdriver.common.by import By


class MainPageEle:
    _add_member_btn = (By.CSS_SELECTOR, "[node-type='addmember']")
    _menu_contacts_tab = (By.CSS_SELECTOR, "[id='menu_contacts']")
    _import_contacts_btn = (By.CSS_SELECTOR, ".ww_indexImg.ww_indexImg_Import")
