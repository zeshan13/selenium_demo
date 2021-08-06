#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 23:10
# @Author  : zeshan
# @File    : import_contact_page.py
import time
from selenium_demo.comm.base_page import BasePage
from selenium_demo.page_obj.contact_page import ContactPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_demo.page_ele.import_contact_page import ImportContactPgaeEle


class ImportContactPgae(BasePage, ImportContactPgaeEle):
    def import_contact_by_file(self, file_path):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self._upload_file_name))
        self.find_element(self._upload_file).send_keys(file_path)
        self.find_element(self._submit_btn).click()
        self.find_element(self._reload_contact_btn).click()
        return ContactPage(self.driver)
