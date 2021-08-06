#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_input.py
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROMEDRIVER = os.path.join(os.path.split(os.path.abspath(__file__))[0], "chromedriver.exe")
JPG_PATH = os.path.join(os.path.split(os.path.abspath(__file__))[0], "piying.jpg")
SLEEP_TIME = 2
URL = "https://image.baidu.com/"

driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
driver.get(URL)
driver.implicitly_wait(5)
time.sleep(SLEEP_TIME)
# 点击上传图片的小图标
driver.find_element(By.ID, "sttb").click()
time.sleep(SLEEP_TIME)
# 向【选择文件】input标签 发送图片
driver.find_element_by_id("stfile").send_keys(JPG_PATH)
# 通过页面title是否变化，判断页面是否跳转
WebDriverWait(driver, 30).until(EC.title_is("百度识图搜索结果"))
driver.quit()
