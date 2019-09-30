# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 9:18
# @Author  : chenky
# @ProjectName :script
# @FileName: test_get_features.py
# @Software: PyCharm

import allure
import pytest
import time

from config.Config import PATH
from public.Log import MyLog
from public.ReadYaml import ReadYamlUtils
from public.Request_tools import RequestTools
_log = MyLog("TestGetFeatures").logger

@allure.story("获取人脸特征模块")
class TestGetFeatures(object):
    data = ReadYamlUtils(PATH("../test_data/2_face_features_get.yaml"))
    __data1 = data.read_data_for_face_detect(PATH("../public/img"), PATH("../public"))["cases"]
    server = RequestTools()

    @pytest.mark.parametrize("data_engine", __data1)
    @pytest.mark.run(order=2)
    @allure.testcase("测试标题")
    def test_01(self, data_engine):
        method = self.data.read_data()["method"]
        url = self.data.read_data()["url"]
        headers = self.server.get_header(self.data.read_data()["sign"])
        body = data_engine["body"]
        _log.info("正在测试{}".format(self.data.read_data()["title"])+"----------"+"测试用例的标题为:{}".format(data_engine["case_title"]))
        res = self.server.send_request(method=method,
                                       url=url,
                                       body=body,
                                       headers=headers)
        if res is not None:
            print(res.text)
        else:
            print(res)

if __name__ == '__main__':
    pytest.main(["-q", "test_get_features.py"])