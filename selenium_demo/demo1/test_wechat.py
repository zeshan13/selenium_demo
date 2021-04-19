#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-18 23:30
# @Author  : zeshan
# @File    : test_wechat.py
import time
# pip install -U selenium
import yaml
from selenium import webdriver
# pip install -U pytest
import pytest
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH = "../tools/chromedriver.exe"
LOGIN_URL = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome"
URL = "https://work.weixin.qq.com/wework_admin/frame"
COOKIES_YAML = "./cookies.yaml"

class TestWeChat:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=option)
        self.driver.maximize_window()


    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # @pytest.mark.skip()
    @pytest.mark.first
    def test_login(self):
        self.driver.get(URL)
        time.sleep(5) #等待扫码
        cookies  = self.driver.get_cookies()
        with open(COOKIES_YAML,"w",encoding="UTF-8") as f:
            yaml.dump(cookies,f)

    @pytest.mark.skip()
    def test_add_member_by_mainpage(self):
        self.driver.get(LOGIN_URL)
        with open(COOKIES_YAML,"r",encoding="UTF-8") as f:
                    cookies = yaml.safe_load(f)
        print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get(URL)
        print(URL)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "[node-type='addmember']").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"[id='username']").send_keys("新员工小菜")
        self.driver.find_element(By.CSS_SELECTOR,"[id='memberAdd_acctid']").send_keys("002")
        self.driver.find_element(By.CSS_SELECTOR,"[id='memberAdd_mail']").send_keys("1222222222@qq.com")
        self.driver.find_element(By.CSS_SELECTOR,"a.qui_btn.ww_btn.js_btn_save").click()
        time.sleep(4)


    def test_add_member_by_contpage(self):
        self.driver.get(LOGIN_URL)
        with open(COOKIES_YAML,"r",encoding="UTF-8") as f:
            cookies = yaml.safe_load(f)
            print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
            self.driver.get(URL)
        print(URL)
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "[id='menu_contacts']").click()
        time.sleep(3)
        # self.driver.find_element(By.CSS_SELECTOR, "a.qui_btn.js_add_member").click()
        self.driver.execute_script("return document.getElementsByClassName('qui_btn ww_btn js_add_member')[0].click()")

        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,"[id='username']").send_keys("新员工小黄")
        self.driver.find_element(By.CSS_SELECTOR,"[id='memberAdd_acctid']").send_keys("003")
        self.driver.find_element(By.CSS_SELECTOR,"[id='memberAdd_mail']").send_keys("1333333333@qq.com")
        self.driver.find_element(By.CSS_SELECTOR,"a.qui_btn.ww_btn.js_btn_save").click()
        time.sleep(3)





