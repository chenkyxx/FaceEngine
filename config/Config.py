# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 17:44
# @Author  : chenky
# @ProjectName :ship_20190828
# @FileName: Config.py
# @Software: PyCharm

import configparser
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ConfigUtils(object):

    def __init__(self, configfile):
        self.config = configparser.ConfigParser()
        self.config.read(configfile, encoding="utf-8")

    def get_sections(self)->list:
        return self.config.sections()

    def get_options_by_sections(self, section):
        return self.config.options(section)

    def get_items_by_sections(self, section):
        return self.config.items(section)

    def get_value_by_section_and_option(self, section, option):
        return self.config.get(section, option)

    def __str__(self):
        return ""
if __name__ == '__main__':
    print(PATH("./"))