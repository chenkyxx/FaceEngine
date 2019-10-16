# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 14:22
# @Author  : chenky
# @ProjectName :ship_20190828
# @FileName: FaceEngine.py
# @Software: PyCharm
import base64
import hashlib
import json
import time
import uuid

import requests

from public.Log import MyLog

_log = MyLog("FaceEngine").logger


class FaceEngine(object):
    __apiKey = "48d534fc6e7f451ca376baaa750729fc"
    __session = requests.session()

    def __init__(self, host):
        self.partner_add = "api/face/partner/add"
        self.partner_update = "api/face/partner/update"
        self.partner_disable = "api/face/partner/disable"
        self.partner_enable = "api/face/partner/enable"
        self.partner_query = "api/face/partner/query"
        self.group_add = "api/face/group/add"
        self.group_update = "api/face/group/update"
        self.group_delete = "api/face/group/delete"
        self.group_list = "api/face/group/list"
        self.face_register = "api/face/mgr/register"
        self.face_remove = "api/face/mgr/remove"
        self.face_clear = "api/face/mgr/clear"
        self.face_get_one_face = "api/face/mgr/single"
        self.face_query_group_faces = "api/face/group/query"
        self.face_identify_detect = "api/face/identify/detect"
        self.face_get_face_features = "api/face/identify/feature"
        self.face_compare_image = "api/face/identify/compareByImage"
        self.face_compare_features = "api/face/identify/compareByFeature"
        self.face_search_image = "api/face/identify/searchByImage"
        self.face_search_features = "api/face/identify/searchByFeature"
        self.face_record_query = "api/face/record/searchQuery"
        self.host = host
        super().__init__()

    @staticmethod
    def get_uuid():
        return str(uuid.uuid1()).replace("-", "")

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

    @staticmethod
    def get_time_stamp():
        """
        获取yyyyMMddHHmmss格式化时间
        :return:
        """
        format_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        return "".join(format_time)

    @staticmethod
    def get_format_time(format_str="%Y-%m-%d %H:%M:%S"):
        """yyyy-MM-dd HH:mm"""
        return "".join(time.strftime(format_str, time.localtime()))

    @staticmethod
    def get_image_to_base64(filename: str):
        try:
            with open(filename, mode="rb") as fp:
                imaga_data = fp.read()
                base64_data = base64.b64encode(imaga_data)
                return str(base64_data, encoding="utf-8")
        except FileNotFoundError:
            _log.error(FileNotFoundError.__name__)

    def get_header(self, sign: str):
        time_stamp = self.get_time_stamp()
        headers = {"content-type": "application/json;charset=utf-8",
                   "timestamp": time_stamp,
                   "apiKey": self.__apiKey,
                   "sign": self.to_md5(sign+time_stamp+self.__apiKey)}
        return headers

    def api_partner_add(self,
                        data_index=0,
                        data="",
                        reqId="",
                        partnerName="",
                        ValidityBegin="",
                        ValidityEnd=""):
        """2.1 新增合作伙伴"""
        if data_index == 0:
            data = {"partnerName": partnerName,
                    "ValidityBegin": ValidityBegin,
                    "ValidityEnd": ValidityEnd}
        else:
            data = data
        body = {"reqId": reqId,
                "data": data}
        res = None
        try:
            res = self.__session.post(url=self.host+self.partner_add,
                                      headers=self.get_header(self.partner_add),
                                      json=body,
                                      verify=False,
                                      timeout=10)
            return res
        except Exception as e:
            print(str(e))
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_partner_update(self,
                        data_index=0,
                        data="",
                        reqId="",
                        partnerId="",
                        partnerName="",
                        ValidityBegin="",
                        ValidityEnd=""):
        """
        2.2 修改合作
        :param data_index:
        :param data:
        :param reqId:
        :param partnerName:
        :param ValidityBegin:
        :param ValidityEnd:
        :return:
        """
        if data_index == 0:
            data = {"partnerId": partnerId,
                    "partnerName": partnerName,
                    "ValidityBegin": ValidityBegin,
                    "ValidityEnd": ValidityEnd}
        else:
            data = data
        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.partner_update,
                                      headers=self.get_header(self.partner_update),
                                      json=body,
                                      verify=False,
                                      timeout=10)
            return res
        except Exception as e:
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_partner_disable(self,
                        data_index=0,
                        data="",
                        reqId="",
                        partnerId=""
                        ):
        """2.3 停用合作伙伴
        描述：停用合作伙伴，使其不能使用人脸引擎"""
        if data_index == 0:
            data = {"partnerId": partnerId}
        else:
            data = data
        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.partner_disable,
                                      headers=self.get_header(self.partner_disable),
                                      json=body,
                                      verify=False,
                                      timeout=10)
            return res
        except Exception as e:
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_partner_enable(self,
                        data_index=0,
                        data="",
                        reqId="",
                        partnerId=""
                        ):
        """2.4 重新启用合作伙伴
            描述：启用合作伙伴"""
        if data_index == 0:
            data = {"partnerId": partnerId}
        else:
            data = data
        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.partner_enable,
                                      headers=self.get_header(self.partner_enable),
                                      json=body,
                                      verify=False,
                                      timeout=10)
            return res
        except Exception as e:
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_partner_query(self,
                          condition_index=0,
                          condition="",
                          reqId="",
                          pageIndex="",
                          pageSize="",
                          partnerName=""):
        """2.5 查询合作伙伴
            描述：分页查询所有航班的信息"""
        if condition_index ==0:
            condition = {"partnerName": partnerName}
        else:
            condition = condition
        body = {"reqId": reqId,
                "pageIndex": pageIndex,
                "pageSize": pageSize,
                "condition": condition}
        try:
            res = self.__session.post(url=self.host+self.partner_query,
                                      headers=self.get_header(self.partner_query),
                                      json=body,
                                      verify=False,
                                      timeout=10)
            return res
        except Exception as e:
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_group_add(self,
                        data_index=0,
                        data="",
                        reqId="",
                        name="",
                        partnerId="",
                        threshold=None
                        ):
        """3.1 新增用户组
            描述：新增管理人脸的组,最多不超过99组。"""
        if data_index == 0:
            data = {"name": name,
                    "partnerId": partnerId,
                    "threshold": threshold}
        else:
            data = data
        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.group_add,
                                      headers=self.get_header(self.group_add),
                                      json=body,
                                      verify=False,
                                      timeout=10)
            return res
        except Exception as e:
            print("请求发送失败"+"\n出错方式为{}".format(str(e)))
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_group_update(self,
                        data_index=0,
                        data="",
                        reqId="",
                        oldName="",
                        newName="",
                        partnerId=""
                        ):
        """3.1 修改用户组
            描述：修改管理人脸的组信息。"""
        if data_index == 0:
            data = {"partnerId": partnerId,
                    "oldName": oldName,
                    "newName": newName}
        else:
            data = data
        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.group_update,
                                      headers=self.get_header(self.group_update),
                                      json=body,
                                      verify=False,
                                      timeout=10)
            return res
        except Exception as e:
            return "请求发送失败"+"\n"+str(e)

    def api_group_delete(self,
                        data_index=0,
                        data="",
                        reqId="",
                        partnerId="",
                        name=""
                        ):
        """3.3 删除组
            描述：删除组信息"""
        if data_index == 0:
            data = {"partnerId": partnerId,
                    "name": name
                    }
        else:
            data = data
        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.group_delete,
                                      headers=self.get_header(self.group_delete),
                                      json=body,
                                      verify=False,
                                      timeout=10)
            return res
        except Exception as e:
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_group_list(self,
                       data_index=0,
                       reqId="",
                       data="",
                       partnerId=""
                        ):
        """3.4 组列表
            描述：列出所有组的组名，删除组后组中注册的人脸会全部清空"""
        if data_index == 0:
            data = {"partnerId": partnerId}
        else:
            data = data
        body = {"reqId": reqId,
                "data": data
                }
        try:
            res = self.__session.post(url=self.host+self.group_list,
                                      headers=self.get_header(self.group_list),
                                      json=body,
                                      verify=False,
                                      timeout=10)
            return res
        except Exception as e:
            print("请求发送失败"+"\n出错方式为{}".format(str(e)))
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_face_register(self,
                          data_index=0,
                          reqId="",
                          data="",
                          partnerId="",
                          groupName="",
                          faceCode="",
                          faceName="",
                          faceImage="",
                          note=""):
        """4.1 人脸注册
        描述：注册人脸到组中，一组中人脸不允许超过 10w人"""
        if data_index == 0:
            data = {"partnerId": partnerId,
                    "groupName": groupName,
                    "faceCode": faceCode,
                    "faceName": faceName,
                    "faceImage": faceImage,
                    "note": note}
        else:
            data = data

        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.face_register,
                                      headers=self.get_header(self.face_register),
                                      json=body,
                                      verify=20)
            return res
        except Exception as e:
            return "请求发送失败"+"\n出错方式为-----{}".format(str(e))

    def api_face_remove(self,
                          data_index=0,
                          reqId="",
                          data="",
                          partnerId="",
                          groupName="",
                          faceCode=""
                          ):
        """4.2 人脸删除
        描述：从组中删除人脸"""
        if data_index == 0:
            data = {"partnerId": partnerId,
                    "groupName": groupName,
                    "faceCode": faceCode
                    }
        else:
            data = data

        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.face_remove,
                                      headers=self.get_header(self.face_remove),
                                      json=body,
                                      verify=20)
            return res
        except Exception as e:
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_face_clear(self,
                          data_index=0,
                          reqId="",
                          data="",
                          partnerId="",
                          groupName=""
                          ):
        """4.3 人脸清空
        描述：从组中清空所有的人脸"""
        if data_index == 0:
            data = {"partnerId": partnerId,
                    "groupName": groupName
                    }
        else:
            data = data

        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.face_clear,
                                      headers=self.get_header(self.face_clear),
                                      json=body,
                                      verify=20)
            return res
        except Exception as e:
            print("请求发送失败"+"\n出错方式为{}".format(str(e)))
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_face_get_one_face(self,
                          data_index=0,
                          reqId="",
                          data="",
                          partnerId="",
                          groupName="",
                          faceCode=""):
        """4.4 获取单个人脸信息
        描述：获取一个人脸的完整信息"""
        if data_index == 0:
            data = {"partnerId": partnerId,
                    "groupName": groupName,
                    "faceCode": faceCode
                    }
        else:
            data = data

        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.face_get_one_face,
                                      headers=self.get_header(self.face_get_one_face),
                                      json=body,
                                      verify=20)
            return res
        except Exception as e:
            print("请求发送失败"+"\n出错方式为{}".format(str(e)))
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_face_query_group_faces(self,
                          condition_index=0,
                          reqId="",
                          pageIndex="",
                          pageSize="",
                          condition="",
                          partnerId="",
                          groupName="",
                          faceCode="",
                          faceName=""):
        """4.5 查看组内人脸信息
        描述：查询当前组内的人脸信息"""
        if condition_index == 0:
            condition = {"partnerId": partnerId,
                         "groupName": groupName,
                         "faceCode": faceCode,
                         "faceName": faceName
                    }
        else:
            condition = condition

        body = {"reqId": reqId,
                "pageIndex": pageIndex,
                "pageSize": pageSize,
                "condition": condition}
        try:
            res = self.__session.post(url=self.host+self.face_query_group_faces,
                                      headers=self.get_header(self.face_query_group_faces),
                                      json=body,
                                      verify=20)
            return res
        except Exception as e:
            print("请求发送失败"+"\n出错方式为{}".format(str(e)))
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_face_identify_detect(self,
                                       data_index=0,
                                       reqId="",
                                       data="",
                                       partnerId="",
                                       image=""
                                       ):
        """5.1 人脸检测
        描述：检测一张图片中的人脸数量以及位置"""
        if data_index == 0:
            data = {"partnerId": partnerId,
                    "image": image
                    }
        else:
            data = data

        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.face_identify_detect,
                                      headers=self.get_header(self.face_identify_detect),
                                      json=body)
            return res
        except Exception as e:
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_face_get_features(self,
                                       data_index=0,
                                       reqId="",
                                       data="",
                                       partnerId="",
                                       image="",
                              type_=0,
                              position=None
                                       ):
        """5.2 获取人脸特征
        描述：检测一张图片中的人脸数量以及位置"""
        if data_index == 0:
            data = {"partnerId": partnerId,
                    "image": image,
                    "type": type_,
                    "position": position
                    }
        else:
            data = data

        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.face_get_face_features,
                                      headers=self.get_header(self.face_get_face_features),
                                      json=body)
            return res
        except Exception as e:
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_face_compare_images(self,
                                       data_index=0,
                                       reqId="",
                                       data="",
                                       partnerId="",
                                       image1="",
                                       image2=""):
        """5.3 人脸比对 - 根据2张图片
        描述：以1比1的方式进行人脸比对"""
        if data_index == 0:
            data = {"partnerId": partnerId,
                    "image1": image1,
                    "image2": image2
                    }
        else:
            data = data

        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.face_compare_image,
                                      headers=self.get_header(self.face_compare_image),
                                      json=body)
            return res
        except Exception as e:
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_face_compare_features(self,
                                       data_index=0,
                                       reqId="",
                                       data="",
                                       partnerId="",
                                       feature1="",
                                       feature2=""):
        """5.4 人脸比对 - 根据2个特征
        描述：以1比1的方式进行人脸比对"""
        if data_index == 0:
            data = {"partnerId": partnerId,
                    "feature1": feature1,
                    "feature2": feature2
                    }
        else:
            data = data

        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.face_compare_features,
                                      headers=self.get_header(self.face_compare_features),
                                      json=body)
            return res
        except Exception as e:
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_face_search_image(self,
                                       data_index=0,
                                       reqId="",
                                       data="",
                                       partnerId="",
                                       image="",
                                       groupName="",
                                       position="",
                                       matchNum=""):
        """5.5 人脸查找 - 根据图片
        描述：以1比N的方式搜索组里面的人脸，返回分数最高的x个结果。"""
        if data_index == 0:
            data = {"partnerId": partnerId,
                    "image": image,
                    "groupName": groupName,
                    "position": position,
                    "matchNum": matchNum
                    }
        else:
            data = data

        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.face_search_image,
                                      headers=self.get_header(self.face_search_image),
                                      json=body)
            return res
        except Exception as e:
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_face_search_features(self,
                                       data_index=0,
                                       reqId="",
                                       data="",
                                       partnerId="",
                                       feature="",
                                       groupName="",
                                       liveImage="",
                                       matchNum=""):
        """5.6 人脸查找 - 根据特征
        描述：以1比N的方式搜索组里面的人脸，返回分数最高的10个结果。"""
        if data_index == 0:
            data = {"partnerId": partnerId,
                    "feature": feature,
                    "groupName": groupName,
                    "liveImage": liveImage,
                    "matchNum": matchNum
                    }
        else:
            data = data

        body = {"reqId": reqId,
                "data": data}
        try:
            res = self.__session.post(url=self.host+self.face_search_features,
                                      headers=self.get_header(self.face_search_features),
                                      json=body)
            return res
        except Exception as e:
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

    def api_face_record_query(self,
                                       condition_index=0,
                                       reqId="",
                                       pageIndex="",
                                       pageSize="",
                                       condition="",
                                       partnerId="",
                                       groupName="",
                                       result="",
                                       beginTime="",
                                       endTime=""):
        """6.1 查询人脸查询记录
        描述：查询人脸查询的记录。"""
        if condition_index == 0:
            condition = {"partnerId": partnerId,
                         "groupName": groupName,
                         "result": result,
                         "beginTime": beginTime,
                         "endTime": endTime
                    }
        else:
            condition = condition

        body = {"reqId": reqId,
                "pageIndex": pageIndex,
                "pageSize": pageSize,
                "condition": condition}
        try:
            res = self.__session.post(url=self.host+self.face_record_query,
                                      headers=self.get_header(self.face_record_query),
                                      json=body)
            return res
        except Exception as e:
            return "请求发送失败"+"\n出错方式为{}".format(str(e))

if __name__ == '__main__':
    aa = FaceEngine(host="http://175.168.0.29:8089/")
    print(FaceEngine.get_format_time())

    # res = aa.api_partner_add(reqId="reqID", partnerName="test_partName", ValidityBegin="2019-10-13 15:36:34",
    #                          ValidityEnd="2020-10-14 15:36:34")
    # print(res.text)
    res = aa.api_group_add(reqId="reqId", name="TestGroupName", partnerId="1409b37cdb58414bbd0fa6ecf1929c33",
                           threshold=0.9)
    print(res.text)






