#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:41
# @Author  : zeshan
# @File    : base_page.py
import yaml

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_demo.comm import config
from selenium_demo.comm.logger import Logger
from selenium_demo.comm.do_yaml import DoYaml
cfg = config.COMMCFG
logger = Logger("base_page.py").getLog()

class BasePage:

    def __init__(self,driver=None):
        if driver == None:
            self.driver = webdriver.Chrome()
            self.driver.get(url=cfg.login_url)
            cookies = DoYaml().read_yaml(file_path=cfg.cookies_path)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get(url=cfg.main_url)
        else:
            self.driver = driver
        self.driver.maximize_window()

    def find_element(self,by,ele=None):
        try:
            if ele == None:
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(by))
                ele_obj = self.driver.find_element(*by)
            else:
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((by,ele)))
                ele_obj = self.driver.find_element(by,ele)
            logger.info("find_element (%s,%s)" % (by, ele))
        except Exception as e:
            logger.error("Failed to find_element (%s,%s) :%s"%(by,ele,e))
        else:
            return ele_obj

    def find_elements(self, by, ele=None):
        try:
            if ele == None:
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(by))
                ele_obj = self.driver.find_element(*by)
            else:
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((by, ele)))
                ele_obj = self.driver.find_element(by, ele)
            logger.info("find_elements (%s,%s)" % (by, ele))
        except Exception as e:
            logger.error("Failed to find_elements (%s,%s) :%s" % (by, ele, e))
        else:
            return ele_obj

    def execute_script(self,js):
        try:
            self.driver.execute_script(js)
            logger.info("execute_script suecess:%s" % js)
        except Exception as e:
            logger.error("Failed to execute_script:%s" % js)


