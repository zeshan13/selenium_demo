#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:41
# @Author  : zeshan
# @File    : add_member_page.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_demo.comm.base_page import BasePage
# from selenium_demo.page_obj.contact_page import ContactPage

from selenium_demo.page_ele.add_member_page import AddMemberPageEle


class AddMemberPage(BasePage, AddMemberPageEle):
    def add_member(self, username, accid, email):
        """
        :param username:
        :param accid:
        :param email:
        :return:
        """
        # 方法内导包，避免循环导包
        from selenium_demo.page_obj.contact_page import ContactPage
        # 输入员工名称
        self.find_element(self._username).send_keys(username)
        # 输入工号
        self.find_element(self._accid).send_keys(accid)
        # 输入邮箱
        self.find_element(self._email).send_keys(email)
        # 点击保存按钮
        self.find_element(self._save_btn).click()
        return ContactPage(self.driver)

    def add_member_failed(self, username, accid, email):
        """
        :param username:
        :param accid:
        :param email:
        :return:
        """
        # 方法内导包，避免循环导包
        from selenium_demo.page_obj.contact_page import ContactPage
        # 输入员工名称
        self.find_element(self._username).send_keys(username)
        # 输入工号
        self.find_element(self._accid).send_keys(accid)
        # 输入邮箱
        self.find_element(self._email).send_keys(email)
        # 点击保存按钮
        self.find_element(self._save_btn).click()
        return ContactPage(self.driver)

    def add_member_continue(self, *members_dic_list):
        """
        :param members_dic_list: 添加成员必填信息dic
        {"username":"新员工","accid":"001","email":"123@qq.com"}
        :return:
        """
        # 方法内导包，避免循环导包
        from selenium_demo.page_obj.contact_page import ContactPage

        for member_dic in members_dic_list:
            # 输入员工名称
            self.find_element(self._username).send_keys(member_dic["username"])
            # 输入工号
            self.find_element(self._accid).send_keys(member_dic["accid"])
            # 输入邮箱
            self.find_element(self._email).send_keys(member_dic["email"])
            # 判断如果是最后一次添加，跳出循环
            if member_dic == members_dic_list[-1]:
                break
            # 点击【保存并继续添加】按钮
            self.find_element(self._save_and_continue_btn).click()
            # 等待保存成功tips出现，再继续条添加
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self._save_succ_tip))
        # 点击【保存】按钮
        self.find_element(self._save_btn).click()
        return ContactPage(self.driver)


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    # 访问扫码登录页面
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    AddMemberPage(driver)
