#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-19 21:03
# @Author  : zeshan
# @File    : test_chrome_debug.py

import time
# pip install -U selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH = "../tools/chromedriver.exe"
LOGIN_URL = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome"
URL = "https://work.weixin.qq.com/wework_admin/frame"
COOKIES_YAML = "./cookies.yaml"

class TestChromeDebug:
    def test_remote(self):
        #1.谷歌浏览器配置到环境变量（桌面右键谷歌浏览器图标->属性，可以找到路径）
        #2.关闭所有谷歌浏览器标签
        #3.谷歌以调试模式启动chrome --remote-debugging-port=9222
        #4.手动点击以调试模式打开的谷歌浏览器，进入要调试的页面，页面保持不关闭
        #5.添加代码，浏览器启动设置为调式模式
        option = webdriver.ChromeOptions()
        option.debugger_address = "127.0.0.1:9222" #确保设置的端口不被占用
        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=option)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, "[node-type='addmember']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[id='username']").send_keys("新员工小菜")
        self.driver.find_element(By.CSS_SELECTOR, "[id='memberAdd_acctid']").send_keys("002")
        self.driver.find_element(By.CSS_SELECTOR, "[id='memberAdd_mail']").send_keys("1222222222@qq.com")
        self.driver.find_element(By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save").click()
        time.sleep(4)

