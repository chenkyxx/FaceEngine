# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 17:00
# @Author  : chenky
# @ProjectName :script
# @FileName: Request_tools.py
# @Software: PyCharm
import hashlib
import uuid

import requests
import time
from public.Log import MyLog
_log = MyLog("RequestTools").logger


class RequestTools(object):
    __apiKey = "48d534fc6e7f451ca376baaa750729fc"

    def __init__(self):
        self.session = requests.session()

    @staticmethod
    def get_uuid():
        return str(uuid.uuid1()).replace("-", "")

    @staticmethod
    def get_time_stamp():
        """
        获取yyyyMMddHHmmss格式化时间
        :return:
        """
        format_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        return "".join(format_time)

    @staticmethod
    def to_md5(str_object):
        """
        将字符串对象转换成md5加密形式
        :param str_object:
        :return:
        """
        md5 = hashlib.md5()
        bytes_object = bytes(str_object, encoding="utf-8")
        md5.update(bytes_object)
        md5_str_object = md5.hexdigest()
        return "".join(md5_str_object)

    def get_header(self, sign: str):
        time_stamp = self.get_time_stamp()
        headers = {"content-type": "application/json;charset=utf-8",
                   "timestamp": time_stamp,
                   "apiKey": self.__apiKey,
                   "sign": self.to_md5(sign+time_stamp+self.__apiKey)}
        return headers

    def send_request(self, method, url: str, body: object, headers=None, cookies=None, json_=True, params=None):
        try:
            if method == "post":
                if url.startswith("http"):
                    if json_:
                        response = self.session.post(url=url, json=body, verify=False, headers=headers, cookies=cookies)
                        return response
                    else:
                        response = self.session.post(url=url, data=body, verify=False, headers=headers, cookies=cookies)
                        return response
                else:
                    _log.warning("url地址必须是以http开头")
                    return False
            elif method == "get":
                if url.startswith("http"):
                    response = self.session.get(url=url, params=params, verify=False, headers=headers, cookies=cookies)
                    return response
                else:
                    _log.warning("url地址必须是以http开头")
            else:
                _log.warning("请求方法没有按照规定,只有get和post")
                return None
        except Exception as e:
            return "{}".format(e)

if __name__ == '__main__':
    aa = RequestTools().send_request(method="post", url="htp://175.168.0.139:8080/aaa", body={"reqId": "wwwwwwwwwwww"})
    print(aa)
    pass

