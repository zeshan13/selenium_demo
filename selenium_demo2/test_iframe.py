#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_iframe.py
import os
import time
from selenium import webdriver

CHROMEDRIVER = os.path.join(os.path.split(os.path.abspath(__file__))[0],"chromedriver.exe")
SLEEP_TIME = 1

driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
driver.get("https://www.w3school.com.cn/tiy/t.asp?f=js_alert")
driver.implicitly_wait(5)
time.sleep(SLEEP_TIME)
# 点击切换主题按钮
driver.find_element_by_xpath('//li[@id="tiy_btn_theme"]/a').click()
time.sleep(SLEEP_TIME)
#切换进iframe
driver.switch_to.frame(driver.find_element_by_id("iframeResult"))
#点击“试一试”按钮
driver.find_element_by_tag_name("button").click()
time.sleep(SLEEP_TIME)
# 点击确定，接受弹窗
driver.switch_to.alert.accept()
time.sleep(SLEEP_TIME)
#切换出iframe
driver.switch_to.default_content()
driver.switch_to.parent_frame()
time.sleep(SLEEP_TIME)
#点击切换主题按钮
driver.find_element_by_xpath('//li[@id="tiy_btn_theme"]/a').click()
time.sleep(SLEEP_TIME)
#关闭浏览器
driver.quit()
