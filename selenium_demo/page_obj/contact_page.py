#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:41
# @Author  : zeshan
# @File    : contact_page.py
from selenium_demo.comm.base_page import BasePage
from add_member_page import AddMemberPage

class ContactPage(BasePage):
    def get_contact_list(self):
        contact_list = []
        return contact_list

    def add_member(self,username, accid, phone):

        return AddMemberPage(self.driver)
