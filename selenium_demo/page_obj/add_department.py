#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 20:49
# @Author  : zeshan
# @File    : add_department.py
from selenium_demo.comm.base_page import BasePage
from selenium.webdriver.common.by import By

class AddDepartment(BasePage):
    _department_name = (By.CSS_SELECTOR, ".qui_inputText.ww_inputText[name='name']")
    _select_department = (By.CSS_SELECTOR, ".js_parent_party_name")
    _root_departments = (By.CSS_SELECTOR, "div.qui_dropdownMenu.ww_dropdownMenu.member_colLeft.js_party_list_container >div > ul >li > a.jstree-anchor")
    _sure_btn = (By.CSS_SELECTOR, "div > a:first-child[d_ck]")
    _cancle_btn = (By.CSS_SELECTOR, "div > a:last-child[d_ck]")

    def add_department(self,name,department=None):
        # 方法内导包，避免循环导包
        from selenium_demo.page_obj.contact_page import ContactPage
        # 输入心中部门名称
        self.find_element(self._department_name).send_keys(name)
        # 点击选择部门下拉框
        self.find_element(self._select_department).click()
        if department == None:
            # 选择根部门
            self.find_element(self._root_departments).click()
        else:
            pass
        # 点击确定按钮
        self.find_element(self._sure_btn).click()
        return ContactPage(self.driver)

