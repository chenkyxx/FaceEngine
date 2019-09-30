# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 11:28
# @Author  : chenky
# @ProjectName :script
# @FileName: test_face_search_features.py
# @Software: PyCharm
import pytest
import time

from config.Config import PATH
from public.Log import MyLog
from public.ReadYaml import ReadYamlUtils
from public.Request_tools import RequestTools
_log = MyLog("TestFaceSearchFeatures").logger


class TestFaceSearchFeatures(object):
    data = ReadYamlUtils(PATH("../test_data/6_face_search_features.yaml"))
    __data1 = data.read_data_for_face_detect(PATH("../public/img"), PATH("../public/features"))["cases"]
    server = RequestTools()

    @pytest.mark.parametrize("data_engine", __data1)
    @pytest.mark.run(order=2)
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
    pytest.main(["-q", "test_face_search_features.py"])

