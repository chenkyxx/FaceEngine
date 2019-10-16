# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 15:47
# @Author  : chenky
# @ProjectName :script
# @FileName: produce_data.py
# @Software: PyCharm
import json
import uuid
from multiprocessing import Process
import time


from config.Config import ConfigUtils, PATH
from public.FaceEngine import FaceEngine
from public.Log import MyLog

_log = MyLog("produce_data").logger
_server = FaceEngine(ConfigUtils(PATH("../config/config.ini")).get_value_by_section_and_option("server", "engine_host"))

""" 1. 进行1个合作伙伴增加
    2.进行10个用户组（人脸库）的增加
    3.对每个用户组进行10W人脸数据的注册
    命名规则：
        伙伴名称：part+int
        组名（人脸库名）：group+int
        人脸代码：伙伴名称+组名+int
        人脸名称：faceName
"""
_picture_path = "C:/chenkeyun/OtherFile/picture/"


def add_one_partner_group():
    # 调用新增合作伙伴接口
    # res = _server.api_partner_add(partnerName="part0", ValidityBegin="2019-10-13 15:36:34", ValidityEnd="2020-10-13 15:36:34")
    # _log.info(res.text)
    # 添加用户组（人脸库）
    for i in range(0, 10):
        res_a = _server.api_group_add(reqId=uuid.uuid1().__str__(), partnerId="0913c3c5cc254692bf8b8b32d148a498", name="group"+str(i),
                                      threshold=0.9)
        _log.info(res_a.text)


class RegisterFace(Process):
    def __init__(self, partnerName, groupName, process_name):
        # partnerName = p1   groupName=g1
        Process.__init__(self)
        self.groupName = groupName
        self.partnerName = partnerName
        self.process_name = process_name

    @staticmethod
    def judge_register(return_obj, status_code):
        try:
            dict_data = None
            try:
                dict_data = json.loads(return_obj.text)
            except Exception:
                return False
            if dict_data is not None:
                assert dict_data["status"] == status_code
                return True
        except Exception:
            return False

    def run(self):
        base_name = self.partnerName+self.groupName
        for index in range(0, 90000):
            res_register = _server.api_face_register(partnerId="", groupName=self.groupName,
                                                     faceCode=base_name+str(index),
                                                     faceName="name"+str(index),
                                                     faceImage=_server.get_image_to_base64(_picture_path+str(index)+".jpg"))
            try:
                if not str(res_register).startswith("请求发送失败"):
                    if self.judge_register(res_register, 0):
                        print("注册成功"+res_register.text)
                    else:
                        _log.error("注册失败，失败的人为:{}".format(index)+self.process_name)
                        continue
                else:
                    _log.error("注册请求发送失败，失败的人为{}".format(index)+self.process_name)
                    continue
            except Exception as e:
                _log.info("出现异常{}".format(e)+self.process_name)
                continue


class MyTest(Process):
    def __init__(self, name_):
        Process.__init__(self)
        self.name_ = name_

    def run(self):
        for i in range(0, 1000000):
            print(1)
        _log.warn(self.name+"结束")


if __name__ == '__main__':
    # add_one_partner_group()
    pass
    # pro_list = []
    # for i in range(0, 10):
    #     pro_list.append(MyTest(name_="name"+str(i)))
    # for pp in pro_list:
    #     pp.start()


