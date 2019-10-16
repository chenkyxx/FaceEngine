# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 10:57
# @Author  : chenky
# @ProjectName :script
# @FileName: test_face_detect.py
# @Software: PyCharm
import json

import pytest
import time

from config.Config import PATH
from public.Assert import AssertResult
from public.Log import MyLog
from public.ReadYaml import ReadYamlUtils
from public.Request_tools import RequestTools
_log = MyLog("TestFaceDetect").logger


class TestFaceDetect(object):
    data = ReadYamlUtils(PATH("../test_data/1_face_identify.yaml"))
    __data1 = data.read_data_for_face_detect(PATH("../public/img"), PATH("../public"))["cases"]
    server = RequestTools()

    @pytest.mark.parametrize("data_engine", __data1)
    @pytest.mark.run(order=2)
    def test_01(self, data_engine):
        method = self.data.read_data()["method"]
        url = self.data.read_data()["url"]+self.data.read_data()["sign"]
        headers = self.server.get_header(self.data.read_data()["sign"])
        body = data_engine["body"]
        titile = data_engine["case_title"]
        if titile == "无人脸时（其他图片），不能检测到人脸的数量及位置":
            if not self.server.get_json_file(body):
                print("'GGGGGGGGGGGGGGGGGG")
        _log.info("正在测试{}".format(self.data.read_data()["title"])+"----------"+"测试用例的标题为:{}".format(data_engine["case_title"]))
        res = self.server.send_request(method=method,
                                       url=url,
                                       body=body,
                                       headers=headers)
        if res is not None and not isinstance(res, str):
            response = res.text
            if AssertResult().judge_code(data_engine["status"], response):
                print(response)
                time.sleep(0.1)
            else:
                raise AssertionError

        else:
            print(res)

if __name__ == '__main__':
    pytest.main(["-q", "test_face_detect.py"])
