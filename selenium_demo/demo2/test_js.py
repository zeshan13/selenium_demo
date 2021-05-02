#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_js.py
import time
from selenium import webdriver

SLEEP_TIME = 3
URL = "https://www.12306.cn/index/"
driver = webdriver.Chrome(executable_path="../tools/chromedriver.exe")
driver.get(URL)
time.sleep(SLEEP_TIME )
#去掉readonly属性，直接输入日期
data_js = 'document.getElementById("train_date").removeAttribute("readonly")'
driver.execute_script(data_js)
#赋值一个新日期
data_js_2 = "document.getElementById('train_date').value='2021-12-32'"
driver.execute_script(data_js_2)
time.sleep(SLEEP_TIME )
driver.quit()
