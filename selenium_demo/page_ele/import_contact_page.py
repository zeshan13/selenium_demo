#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 23:10
# @Author  : zeshan
# @File    : import_contact_page.py
from selenium.webdriver.common.by import By


class ImportContactPgaeEle:
    _upload_file = (By.CSS_SELECTOR, "input.qui_btn.ww_btn.ww_fileInputWrap")
    _submit_btn = (By.CSS_SELECTOR, "#submit_csv")
    _reload_contact_bn = (By.CSS_SELECTOR, "#reloadContact")
    _upload_file_name = (By.CSS_SELECTOR, "#upload_file_name")
