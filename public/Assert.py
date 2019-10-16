# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 16:24
# @Author  : chenky
# @ProjectName :script
# @FileName: Assert.py
# @Software: PyCharm
from public.Log import MyLog
import json


class AssertResult(object):
    __log = MyLog("AssertResult").logger
    __response = None

    def __init__(self):
        pass

    def assert_body(self, json_:str):
        """
        断言请求的json格式的字符串，以断言请求是否成功
        :param json_: 请求返回的json的字符串
        :return:
        """
        try:
            result_list = []
            dict_object = json.loads(json_)
            self.__log.info("http请求发送成功")
            result_list.append(True)
            result_list.append(dict_object)
            return result_list
        except Exception:
            return False

    def judge_code(self, status: int, json_: str):
        """
        对响应的status进行断言
        :param status:
        :param json_:
        :return:
        """
        void = self.assert_body(json_)
        if void:
            dict_obj = void[1]
            try:
                if dict_obj["status"] == status:
                    self.__log.info("断言正常，status为{}".format(status))
                    return True
                else:
                    self.__log.warning("业务不正常,status 不满足0"+"-----当前的status的值为{}".format(dict_obj["status"]))
                    return False
            except Exception as e:
                self.__log.error("服务器返回出错，json体中没有status字段+\n+{}".format(e))
                return False
        else:
            self.__log.error("xxxxx")
if __name__ == '__main__':

    # def aa(test, index):
    #     print(test, index)
    # a = {"test": 1, "index": 2}
    # aa(**a)

    m = {"test": None, "test2": 2}
    for key in m:
        print(key, str(m[key]).endswith("test"))
        print()
