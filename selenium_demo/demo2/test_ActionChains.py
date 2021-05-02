#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_ActionChains.py
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

SLEEP_TIME = 3
URL = "https://www.runoob.com/try/try.php?filename=tryhtml5_ev_onmousedown"
driver = webdriver.Chrome(executable_path="../tools/chromedriver.exe")
driver.get(URL)
driver.implicitly_wait(5)
# 切换iframe
driver.switch_to.frame(driver.find_element_by_id("iframeResult"))
# 定位p元素
p = driver.find_element_by_id("p1")
actions = ActionChains(driver)
#点击并保持
actions.click_and_hold(p)
# 执行
actions.perform()
time.sleep(SLEEP_TIME)
driver.quit()