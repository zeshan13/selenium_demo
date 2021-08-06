#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 20:49
# @Author  : zeshan
# @File    : add_department_page.py
from selenium_demo.comm.base_page import BasePage
from selenium_demo.page_ele.add_department_page import AddDepartmentEle


class AddDepartment(BasePage, AddDepartmentEle):

    def add_department(self, name, department=None):
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
