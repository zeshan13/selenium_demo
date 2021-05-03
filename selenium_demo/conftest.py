#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 12:16
# @Author  : zeshan
# @File    : conftest.py
import time

import allure
from selenium import webdriver
import pytest
from selenium_demo.comm import config
from selenium_demo.comm.do_yaml import DoYaml
from typing import List
from selenium_demo.page_obj.main_page import MainPage

cfg = config.COMMCFG
COOKIES = False
_driver = None

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

@pytest.fixture(scope="session")
def driver():
    global  _driver
    _driver = webdriver.Chrome(executable_path=cfg.chromedriver_path)
    _driver.get(url=cfg.login_url)
    time.sleep(3)
    yield _driver
    _driver.quit()


@pytest.fixture
def cookies():
    cookies = DoYaml().read_yaml(file_path=cfg.cookies_path)
    return cookies

@pytest.fixture
def main_page(driver,cookies):
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(url=cfg.main_url)
    _main_page = MainPage(driver)
    return _main_page




@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅获取用例call且执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图..'):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
    # 参考：https://www.cnblogs.com/yoyoketang/p/12609871.html