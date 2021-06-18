#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 22:55
# @Author  : zeshan
# @File    : do_yaml.py

# pip install pyyaml
import yaml
import os


class DoYaml:
    def read_yaml(self,file_path):
        with open(file_path,encoding='utf-8') as f:
            datas = yaml.safe_load(f)
        return datas

    def write_yaml(self,file_path,content):
        with open(file_path, "w", encoding="UTF-8") as f:
            yaml.dump(content, f)


if __name__ == '__main__':
    from selenium_demo.selenium_demo.comm import config
    CFG = config.COMMCFG
    cookies_path = CFG.COOKIES_PATH
    init_datas_path = os.path.join(CFG.TEST_DATAS_DIR,"init_datas_count.yaml")

    t = DoYaml()
    datas = t.read_yaml(file_path=init_datas_path)
    print(datas)

