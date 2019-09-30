# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 17:50
# @Author  : chenky
# @ProjectName :script
# @FileName: ReadYaml.py
# @Software: PyCharm
import base64
import json
import yaml
import re
from config.Config import PATH
from public.Log import MyLog

_log = MyLog("ReadYamlUtils").logger


class ReadYamlUtils(object):
    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def get_image_to_base64(filename: str):
        try:
            with open(filename, mode="rb") as fp:
                imaga_data = fp.read()
                base64_data = base64.b64encode(imaga_data)
                return str(base64_data, encoding="utf-8")
        except FileNotFoundError:
            _log.error(FileNotFoundError.__name__)

    @staticmethod
    def get_txt(txt_filename: str):
        try:
            with open(txt_filename, "r") as fp:
                data = fp.read().rstrip()
                return str(data)
        except Exception as e:
            _log.error("读取文件出现异常{}".format(e))
            return None

    def read_data(self):
        try:
            with open(self.filename, encoding="utf-8") as fp:
                response_content = yaml.load(fp, Loader=yaml.FullLoader)
                return response_content
        except Exception as e:
            print("{}".format(e))

    @staticmethod
    def judge_object(object_for: object, for_type)->bool:
        try:
            if not isinstance(object_for, for_type):
                return False
            else:
                return True
        except Exception as e:
            _log.error("判断对象类型发生了异常----{}".format(e))
            return False

    def read_data_for_face_detect(self, picture_path=None,
                                  features_path=None):
        """
        将yaml中有图片的数据转换成base64编码的数据，再进行返回, 将yaml中features值以
        读取txt文件的方式返回，如果不是txt文件，则默认使用yaml的默认数据
        :param picture_path: 图片路径
        :param features_path: features文件路径
        :return:
        """
        try:
            response_content = None
            pattern_ = re.compile(".*image.*")
            with open(self.filename, encoding="utf-8") as fp:
                response_content = yaml.load(fp, Loader=yaml.FullLoader)
                if not isinstance(response_content, dict):
                    _log.info("返回数据不是dict，请检查yaml的数据格式")
                else:
                    case_data_all = response_content["cases"]
                    # case_data_all ->list
                    for case_one in case_data_all:
                        body_data = dict(case_one["body"])
                        judge_if_exist_key = body_data.get("data")
                        if judge_if_exist_key is not None and self.judge_object(judge_if_exist_key, dict):
                            json_data = dict(body_data["data"])
                            for key in json_data:
                                try:
                                    if str(key).find("feature") >= 0:
                                        feature_value = json_data[key]
                                        if str(feature_value).endswith(".txt"):
                                            str_key_feature_value = self.get_txt(features_path+"/"+feature_value)
                                            if str_key_feature_value is not None:
                                                json_data[key] = str_key_feature_value
                                            else:
                                                pass
                                        else:
                                            pass
                                    elif str(key).find("image") >= 0:
                                        str_key = pattern_.match(str(key)).group(0)
                                        image_name = json_data[str_key]
                                        if str(image_name).endswith("jpg"):
                                            str_key_image_value = self.get_image_to_base64(picture_path+"/"+image_name)
                                            if str_key_image_value is not None:
                                                json_data[str_key] = str_key_image_value
                                            else:
                                                json_data[str_key] = json_data[str_key]
                                    else:
                                        # _log.warning("不是jpg图片或者txt，此时key的值为---{}-----，对应的值为yaml原来的值".format(key))
                                        pass

                                except Exception as e:
                                    continue
                            body_data["data"] = json_data
                            case_one["body"] = body_data
                        else:
                            _log.error("data对应的key不存在，或者，data对应的数据不是json对象")
                    response_content["cases"] = case_data_all
                    return response_content
        except Exception as e:
            _log.error("处理处理发生错误+\n{}".format(e))

if __name__ == '__main__':
    name = PATH("../test_data/1_face_identify.yaml")
    x = ReadYamlUtils(name)
    print(x.read_data())
    print(type(x.read_data()))
    kk = {"55test222": 1, "test2": ".jpg"}
    str_a = "testimagetest"
    pattern = re.compile(".*image.*")
    print(pattern.match(str_a).group(0))
    mm = x.read_data_for_face_detect(PATH("../public/"), ".")
    kk = json.dumps(mm, ensure_ascii=False, indent=2)
    print(kk)