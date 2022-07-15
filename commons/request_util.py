import json
import re

import jsonpath
import requests
from commons.yaml_util import write_yaml


class RequestUtil:
    # 初始化session对象
    sess = requests.session()

    # 规范YAML测试用例
    def standard_yaml_testcases(self, caseinfo):
        """
        :param caseinfo: Yaml测试用例数据
        :return: 无返回
        """

        # 判断YAML测试用例文件是否正确
        caseinfo_keys = caseinfo.keys()
        if "name" and "request" and "validate" in caseinfo_keys:
            request_key = caseinfo["request"].keys()
            if "method" and "url" in request_key:

                # 取得二级关键字，并从request字典中删除
                method = caseinfo["request"].pop("method")
                url = caseinfo["request"].pop("url")

                # **caseinfo["request"]，将去除了method和url的request字典剩余参数进行解包
                # 解包之后，剩余参数以独立键值对的形式传入send_request方法的kwargs参数中
                # 传入形式：param = xxx，headers = xxx。
                res = self.send_request(method, url, **caseinfo["request"])

                # 获得文本格式的返回结果
                text_result = res.text

                # 获取json格式的返回结果
                json_result = ""
                try:
                    json_result = res.json()
                except:
                    print("返回的数据不是json数据格式")

                # 提取需要的关联数据并写入extract.yaml文件
                # 只支持正则提取和jsonpath提取
                if "extract" in caseinfo.keys():
                    for key, value in caseinfo["extract"].items():
                        # 正则提取中间关联变量
                        if "(.*?)" in value or "(.+?)" in value:
                            regular_value = re.search(value, text_result)
                            if regular_value:
                                data = {key: regular_value.group(1)}
                                write_yaml("extract.yaml", data)
                            else:
                                print("extract中间变量提取失败，请检查正则提取表达式")
                        # jsonpath提取中间关联变量,仅仅支持json格式数据
                        else:
                            js_value = jsonpath.jsonpath(json_result, value)
                            if js_value:
                                data = {key: js_value[0]}
                                write_yaml("extract.yaml", data)
                            else:
                                print("extract中间变量提取失败，请检查jsonpath提取表达式")
            else:
                print("用例必须包含二级关键字：method，url")
        else:
            print("用例必须包含一级关键字：name request validate")

# 统一请求封装
    def send_request(self, method, url, **kwargs):
        """
        :param method: 接口请求方法
        :param url: 接口请求url
        :param kwargs: 其他请求数据
        :return: 请求结果
        """
        # method统一小写
        method = str(method).lower()

        # url通过${变量名}取值

        # headers通过${变量名}取值

        # params,data,json通过${变量名}取值

        res = RequestUtil.sess.request(method, url, **kwargs)
        return res

    # 封装替换取值(获取中间变量)的方法
    # 注意1：取值可能的是(url, params, data, json, headers)
    # 注意2：各种数据类型的切换：(int,float,string,list,dict)
    def replace_get_value(self, data):
        """
        :param data: 需要进行转换的数据
        :return:
        """
        if data:
            data_type = type(data)
            if isinstance(data, list) or isinstance(data, dict):
                # 只有字符串才能进行替换
                # 如果传入数据是列表或者字典，则对其进行序列化转化为字符串
                str_data = json.dumps(data)
            else:
                str_data = str(data)

            # 替换


        else:
            print("None不需要通过${变量名}取值")

