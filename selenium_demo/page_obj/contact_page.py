#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:41
# @Author  : zeshan
# @File    : contact_page.py
import time

from selenium_demo.comm.base_page import BasePage
from selenium_demo.page_obj.add_member_page import AddMemberPage
from selenium.webdriver.common.by import By

class ContactPage(BasePage):
    _username = (By.CSS_SELECTOR, "[id='username']")
    _accid = (By.CSS_SELECTOR, "[id='memberAdd_acctid']")
    _email  = (By.CSS_SELECTOR, "[id='memberAdd_mail']")
    _save_btn = (By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save")
    _contact_name_list = (By.CSS_SELECTOR,"#member_list > tr> td:nth-child(2) > span:nth-child(1)")
    _contact_name_list_by_import = (By.CSS_SELECTOR,"[class='js_unsortable js_list']>tr>td:nth-child(2)")
    _batch_import_or_export_btn = (By.CSS_SELECTOR,".ww_btn_PartDropdown_left")
    _import_by_file_btn = (By.CSS_SELECTOR,"#js_contacts48 > div > div.member_colRight > div > div.js_party_info > div.js_has_member > div.js_operationBar_footer.ww_operationBar > div.ww_btnWithMenu.ww_btnWithMenu_Open_Up.js_btnWithMenu.js_import_other_wrap.ww_btnWithMenu_Open > div > ul > li:nth-child(1) > a")

    def get_contact_list(self):
        contact_list = []
        contact_name_list = [i.text for i in self.find_elements(self._contact_name_list)]
        try:
            contact_name_list_by_import = [i.text for i in self.find_elements(self._contact_name_list_by_import)]
        except Exception as e:
            print("Failed to get contact list by import:%s" % e)
        else:
            contact_list.append(contact_name_list_by_import)
        contact_list.append(contact_name_list)
        return contact_list


    def goto_add_member(self):
        # 调用js点击"添加员工"按钮
        time.sleep(5)
        self.execute_script("document.getElementsByClassName('qui_btn ww_btn js_add_member')[0].click()")
        return AddMemberPage(self.driver)

    def goto_import_contacts_by_file(self):
        self.find_element(self._batch_import_or_export_btn)
        self.find_element(self._import_by_file_btn)


