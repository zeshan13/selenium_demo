#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:41
# @Author  : zeshan
# @File    : contact_page.py
import time
from selenium_demo.comm.base_page import BasePage
from selenium_demo.page_obj.add_member_page import AddMemberPage
from selenium_demo.page_obj.add_department import AddDepartment
from selenium_demo.comm.logger import Logger

from selenium_demo.page_ele.contact_page import ContactPageEle

logger = Logger("contact.py").getLog()


class ContactPage(BasePage, ContactPageEle):
    def get_contact_list(self):
        time.sleep(3)
        contact_list = []
        try:
            contact_name_list = [i.text for i in self.find_elements(self._contact_name_list)]
            contact_list = contact_name_list + contact_list
            logger.info("contact_name_list is :%s" % contact_name_list)
        except Exception as e:
            logger.error("Failed to get contact list by import:%s" % e)
        else:
            contact_list = contact_name_list

        try:
            contact_name_list_by_import = [i.text for i in self.find_elements(self._contact_name_list_by_import)]
            logger.info("contact_name_list_by_import is :%s" % contact_name_list_by_import)
        except Exception as e:
            logger.error("Failed to get contact list by import:%s" % e)
        else:
            contact_list = contact_name_list_by_import + contact_list
            logger.info("contact_list is :%s" % contact_list)
        return contact_list

    def goto_add_member(self):
        # 调用js点击"添加员工"按钮
        time.sleep(5)
        self.execute_script("document.getElementsByClassName('qui_btn ww_btn js_add_member')[0].click()")
        return AddMemberPage(self.driver)

    def goto_import_contacts_by_file(self):
        from selenium_demo.page_obj.import_contact_page import ImportContactPgae
        self.find_element(self._batch_import_or_export_btn).click()
        self.find_element(self._import_by_file_btn).click()
        return ImportContactPgae(self.driver)

    def goto_add_department(self):
        self.find_element(self._add).click()
        self.find_element(self._add_department).click()
        return AddDepartment(self.driver)

    def get_department_list(self):
        time.sleep(5)
        department_list = [i.text for i in self.find_elements(self._department_list)]
        return department_list
