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
    _upload_file = (By.CSS_SELECTOR,"input.qui_btn.ww_btn.ww_fileInputWrap")
    _submit_btn = (By.CSS_SELECTOR,"#submit_csv")
    _reload_contact_btn = (By.CSS_SELECTOR,"#reloadContact")

    def import_contact_by_file(self,file_path):
        self.find_element(self._upload_file).send_keys(file_path)
        self.find_element(self._submit_btn).click()
        self.find_element(self._reload_contact_btn).click()
        return ContactPage(self.driver)