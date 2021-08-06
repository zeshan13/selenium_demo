#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-20 23:41
# @Author  : zeshan
# @File    : contact_page.py

from selenium.webdriver.common.by import By


class ContactPageEle:
    _username = (By.CSS_SELECTOR, "[id='username']")
    _accid = (By.CSS_SELECTOR, "[id='memberAdd_acctid']")
    _email = (By.CSS_SELECTOR, "[id='memberAdd_mail']")
    _save_btn = (By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save")
    _contact_name_list = (By.CSS_SELECTOR, "#member_list > tr> td:nth-child(2) > span:nth-child(1)")
    _contact_name_list_by_import = (By.CSS_SELECTOR, ".js_unsortable.js_list.ui-sortable>tr>td:nth-child(2)")
    _batch_import_or_export_btn = (By.CSS_SELECTOR, "div.js_has_member >div >div> a >.ww_btn_PartDropdown_right")
    _import_by_file_btn = (By.CSS_SELECTOR,
                           "div.js_has_member > div > div > div>ul>li>a.qui_dropdownMenu_itemLink.ww_dropdownMenu_itemLink.js_import_member")
    _add = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    _add_department = (By.CSS_SELECTOR, ".js_create_party")
    _department_list = (By.CSS_SELECTOR, "div.member_colLeft_bottom > div > ul  >li >ul >li >a")
