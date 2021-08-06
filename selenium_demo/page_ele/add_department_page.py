#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 20:49
# @Author  : zeshan
# @File    : add_department_page.py
from selenium.webdriver.common.by import By


class AddDepartmentEle:
    _department_name = (By.CSS_SELECTOR, ".qui_inputText.ww_inputText[name='name']")
    _select_department = (By.CSS_SELECTOR, ".js_parent_party_name")
    _root_departments = (By.CSS_SELECTOR,
                         "div.qui_dropdownMenu.ww_dropdownMenu.member_colLeft.js_party_list_container >div > ul >li > a.jstree-anchor")
    _sure_btn = (By.CSS_SELECTOR, "div > a:first-child[d_ck]")
    _cancle_btn = (By.CSS_SELECTOR, "div > a:last-child[d_ck]")
