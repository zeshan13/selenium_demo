#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 23:10
# @Author  : zeshan
# @File    : import_contact_page.py
import time

from selenium_demo.comm.base_page import BasePage
from selenium_demo.page_obj.contact_page import ContactPage
from selenium.webdriver.common.by import By

class ImportContactPgae(BasePage):
    def import_contact_by_file(self):

        return ContactPage(self.driver)