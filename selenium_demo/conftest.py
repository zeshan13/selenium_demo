#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 12:16
# @Author  : zeshan
# @File    : conftest.py
import time

from selenium import webdriver
import pytest
from selenium_demo.comm import config
from selenium_demo.comm.do_yaml import DoYaml
from typing import List
from selenium_demo.page_obj.main_page import MainPage

cfg = config.COMMCFG

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

@pytest.fixture
def driver():
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

