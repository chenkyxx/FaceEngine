# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 11:19
# @Author  : chenky
# @ProjectName :script
# @FileName: test_Api.py
# @Software: PyCharm
import json
import unittest
import sys

from config.Config import ConfigUtils, PATH
from public.Assert import AssertResult
from public.FaceEngine import FaceEngine


class TestApi(unittest.TestCase):
    __config = ConfigUtils(PATH("../config/config.ini"))
    __server = FaceEngine(__config.get_value_by_section_and_option("server", "engine_host"))
    __assert = AssertResult()

    def a(self):
        print(self.__config.get_value_by_section_and_option("server", "engine_host"))

    def test_0_face_register(self):
        """人脸注册"""
        res = self.__server.api_face_register(reqId="11",
                                              partnerId="",
                                              groupName="",
                                              faceCode="",
                                              faceName=self.__server.get_image_to_base64("11"),
                                              faceImage="")
        try:
            self.__assert.judge_code(-1, res.text)
            json_format = json.dumps(eval(res.text), ensure_ascii=False, indent=2)
            print("\n"+json_format)
        except Exception as e:
            print(res+"\n"+"{}".format(e), file=sys.stderr)

    def test_1_face_remove(self):
        """人脸删除"""
        res = self.__server.api_face_remove(reqId="",
                                            partnerId="",
                                            groupName="",
                                            faceCode="")
        try:
            json_format = json.dumps(eval(res.text), ensure_ascii=False, indent=2)
            print("\n"+json_format)
        except Exception as e:
            print(res+"\n"+"{}".format(e), file=sys.stderr)

    def test_2_face_clear(self):
        """人脸清空"""
        res = self.__server.api_face_clear(reqId="",
                                           partnerId="",
                                           groupName="")
        try:
            json_format = json.dumps(eval(res.text), ensure_ascii=False, indent=2)
            print("\n"+json_format)
        except Exception as e:
            print(res+"\n"+"{}".format(e), file=sys.stderr)

    def test_3_get_one_face(self):
        """获取单个人脸信息"""
        res = self.__server.api_face_get_one_face(reqId="",
                                                  partnerId="",
                                                  groupName="",
                                                  faceCode="")
        try:
            json_format = json.dumps(eval(res.text), ensure_ascii=False, indent=2)
            print("\n"+json_format)
        except Exception as e:
            print(res+"\n"+"{}".format(e), file=sys.stderr)

    def test_4_query_group_faces(self):
        """查询当前组内人脸信息"""
        res = self.__server.api_face_query_group_faces(reqId="",
                                                       pageIndex="",
                                                       pageSize="",
                                                       partnerId="",
                                                       groupName="",
                                                       faceCode="",
                                                       faceName="")
        try:
            json_format = json.dumps(eval(res.text), ensure_ascii=False, indent=2)
            print("\n"+json_format)
        except Exception as e:
            print(res+"\n"+"{}".format(e), file=sys.stderr)

    def test_5_face_detect(self):
        """人脸检测"""
        res = self.__server.api_face_identify_detect(reqId="", partnerId="", image="")

        try:
            json_format = json.dumps(eval(res.text), ensure_ascii=False, indent=2)
            print("\n"+json_format)
        except Exception as e:
            print(res+"\n"+"{}".format(e), file=sys.stderr)

    def test_6_face_get_features(self):
        """人脸特征提取"""
        res = self.__server.api_face_get_features(reqId="",
                                                  partnerId="", image="", type_=0, position=None)
        try:
            json_format = json.dumps(eval(res.text), ensure_ascii=False, indent=2)
            print("\n"+json_format)
        except Exception as e:
            print(res+"\n"+"{}".format(e), file=sys.stderr)

    def test_6_face_compare_by_images(self):
        """根据两张图片进行比对"""
        res = self.__server.api_face_compare_images(reqId="",
                                                    partnerId="",
                                                    image1="",
                                                    image2="")
        try:
            json_format = json.dumps(eval(res.text), ensure_ascii=False, indent=2)
            print("\n"+json_format)
        except Exception as e:
            print(res+"\n"+"{}".format(e), file=sys.stderr)

    def test_7_face_compare_by_features(self):
        """根据两个特征进行比对"""
        res = self.__server.api_face_compare_features(reqId="",
                                                      partnerId="",
                                                      feature1="",
                                                      feature2="")
        try:
            json_format = json.dumps(eval(res.text), ensure_ascii=False, indent=2)
            print("\n"+json_format)
        except Exception as e:
            print(res+"\n"+"{}".format(e), file=sys.stderr)

    def test_8_face_search_by_image(self):
        """人脸查找 根据图片"""
        res = self.__server.api_face_search_image(reqId="",
                                                  partnerId="",
                                                  image="",
                                                  groupName="",
                                                  position="",
                                                  matchNum="")
        try:
            json_format = json.dumps(eval(res.text), ensure_ascii=False, indent=2)
            print("\n"+json_format)
        except Exception as e:
            print(res+"\n"+"{}".format(e), file=sys.stderr)

    def test_9_face_search_by_feature(self):
        """人脸查找 根据特征"""
        res = self.__server.api_face_search_features(reqId="",
                                                     partnerId="",
                                                     feature="",
                                                     groupName="",
                                                     liveImage="",
                                                     matchNum="")
        try:
            json_format = json.dumps(eval(res.text), ensure_ascii=False, indent=2)
            print("\n"+json_format)
        except Exception as e:
            print(res+"\n"+"{}".format(e), file=sys.stderr)

    def test_9_9_face_record_query(self):
        """人脸记录查询"""
        res = self.__server.api_face_record_query(reqId="",
                                                  pageIndex="",
                                                  pageSize="",
                                                  partnerId="",
                                                  groupName="",
                                                  result="",
                                                  beginTime="",
                                                  endTime="")
        try:
            json_format = json.dumps(eval(res.text), ensure_ascii=False, indent=2)
            print("\n"+json_format)
        except Exception as e:
            print(res+"\n"+"{}".format(e), file=sys.stderr)

if __name__ == '__main__':
    unittest.main()