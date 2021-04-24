#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:41
# @Author  : zeshan
# @File    : contact_page.py
import time
from selenium_demo.comm.base_page import BasePage
from selenium_demo.page_obj.add_member_page import AddMemberPage
from selenium_demo.page_obj.add_department import AddDepartment
from selenium.webdriver.common.by import By
from selenium_demo.comm.logger import Logger
logger = Logger("contact.py").getLog()

class ContactPage(BasePage):
    _username = (By.CSS_SELECTOR, "[id='username']")
    _accid = (By.CSS_SELECTOR, "[id='memberAdd_acctid']")
    _email  = (By.CSS_SELECTOR, "[id='memberAdd_mail']")
    _save_btn = (By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save")
    _contact_name_list = (By.CSS_SELECTOR,"#member_list > tr> td:nth-child(2) > span:nth-child(1)")
    _contact_name_list_by_import = (By.CSS_SELECTOR,".js_unsortable.js_list.ui-sortable>tr>td:nth-child(2)")
    _batch_import_or_export_btn = (By.CSS_SELECTOR,"div.js_has_member >div >div> a >.ww_btn_PartDropdown_right")
    _import_by_file_btn = (By.CSS_SELECTOR,"div.js_has_member > div > div > div>ul>li>a.qui_dropdownMenu_itemLink.ww_dropdownMenu_itemLink.js_import_member")
    _add = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    _add_department = (By.CSS_SELECTOR, ".js_create_party")
    _department_list = (By.CSS_SELECTOR, "div.member_colLeft_bottom > div > ul  >li >ul >li >a")

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