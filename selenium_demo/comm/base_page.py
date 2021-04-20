#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:41
# @Author  : zeshan
# @File    : base_page.py
import yaml

from selenium import webdriver

class BasePage:

    def __init__(self,driver=None):
        if driver == None:
            self.driver = webdriver.Chrome()
            self.driver.get(url="https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
            with open("cookies.yaml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
                print(yaml_data)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
        else:
            self.driver = driver
        self.driver.maximize_window()

    def find_element(self,by,ele=None):

        if ele == None:
            self.driver.find_element(*by)
        else:
            self.driver.find_element(by,ele)

    def find_elements(self, by, ele=None):
        if ele == None:
            self.driver.find_elements(*by)
        else:
            self.driver.find_elements(by, ele)





