#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : conftest.py.py
import os
import time

import allure
from selenium import webdriver
import pytest
from typing import List

_driver = None

CHROMEDRIVER_PATH = "./chromedriver.exe"
LOGIN_URL = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome"
URL = "https://work.weixin.qq.com/wework_admin/frame"
COOKIES_YAML = "./cookies.yaml"

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

@pytest.fixture(scope='session')
def driver():
    global _driver
    _driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    # _driver.get(url=LOGIN_URL)
    time.sleep(3)
    yield _driver
    time.sleep(3)
    _driver.quit()


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
            with allure.step('添加失败截图...'):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
    # 参考：https://www.cnblogs.com/yoyoketang/p/12609871.html