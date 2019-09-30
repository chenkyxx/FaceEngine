# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 15:35
# @Author  : chenky
# @ProjectName :script
# @FileName: run_all_case.py
# @Software: PyCharm
from config.Config import PATH
import os


def run():
    current_path = PATH("../")
    command = "cd {}".format(current_path)
    print(command)
    run_comm = "pytest -s -q --alluredir report"
    make_report = "allure generate report/ -o report/html"
    a = os.system("c:")
    print(a)
    b = os.system(command)
    print(b)
    c = os.system(run_comm)
    print(c)
    d = os.system(make_report)

if __name__ == '__main__':
    # print(PATH("../"))
    run()
