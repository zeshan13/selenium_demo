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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROMEDRIVER_PATH = "./chromedriver.exe"
LOGIN_URL = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome"
URL = "https://work.weixin.qq.com/wework_admin/frame"
COOKIES_YAML = "./cookies.yaml"


class TestWeChat:
    def setup(self):
        option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
        self.driver.maximize_window()

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.skip()
    @pytest.mark.first
    def test_login(self):
        self.driver.get(LOGIN_URL)
        time.sleep(5)  # 等待扫码
        cookies = self.driver.get_cookies()
        with open(COOKIES_YAML, "w", encoding="UTF-8") as f:
            yaml.dump(cookies, f)

    # @pytest.mark.skip()
    def test_add_member_by_mainpage(self):
        # 打开登录页面
        self.driver.get(LOGIN_URL)
        # 读取yaml文件中的cookies
        with open(COOKIES_YAML, "r", encoding="UTF-8") as f:
            cookies = yaml.safe_load(f)
        # 循环添加cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 打开企业微信主页面
        self.driver.get(URL)
        # 点击添加员工
        addmember_locator = (By.CSS_SELECTOR, "[node-type='addmember']")
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(addmember_locator))
        self.driver.find_element(*addmember_locator).click()
        # 输入员工名称
        username_locator = (By.CSS_SELECTOR, "[id='username']")
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(username_locator))
        self.driver.find_element(*username_locator).send_keys("新员工小菜")
        # 输入工号
        self.driver.find_element(By.CSS_SELECTOR, "[id='memberAdd_acctid']").send_keys("009")
        # 输入邮箱
        self.driver.find_element(By.CSS_SELECTOR, "[id='memberAdd_mail']").send_keys("1222222222@qq.com")
        # 点击保存按钮
        self.driver.find_element(By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save").click()
        time.sleep(4)

    # @pytest.mark.skip()
    def test_add_member_by_contpage(self):
        # 打开登录页面
        self.driver.get(LOGIN_URL)
        # 读取yaml文件中的cookies
        with open(COOKIES_YAML, "r", encoding="UTF-8") as f:
            cookies = yaml.safe_load(f)
        # 循环添加cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 打开企业微信主页面
        self.driver.get(URL)
        # 点击"通讯录"标签页
        menu_contacts_locator = (By.CSS_SELECTOR, "[id='menu_contacts']")
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(menu_contacts_locator))
        self.driver.find_element(*menu_contacts_locator).click()
        # 调用js点击"添加员工"按钮
        time.sleep(5)
        self.driver.execute_script("document.getElementsByClassName('qui_btn ww_btn js_add_member')[0].click()")
        # 输入员工名称
        username_locator = (By.CSS_SELECTOR, "[id='username']")
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(username_locator))
        self.driver.find_element(*username_locator).send_keys("新员工小黄")
        # 输入工号
        self.driver.find_element(By.CSS_SELECTOR, "[id='memberAdd_acctid']").send_keys("008")
        # 输入邮箱
        self.driver.find_element(By.CSS_SELECTOR, "[id='memberAdd_mail']").send_keys("1222222223@qq.com")
        # 点击保存按钮
        self.driver.find_element(By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save").click()
        time.sleep(2)
