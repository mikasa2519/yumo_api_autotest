import random
import re

import pytest

from commons.request_util import RequestUtil
from commons.yaml_util import write_yaml, read_extract_yaml, read_testcase_yaml


class TestApi:

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/get_token.yaml"))
    def test_get_token(self, caseinfo):
        names = caseinfo["name"]
        methods = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]
        headers = caseinfo["request"]["headers"]
        datas = caseinfo["request"]["params"]
        validatas = caseinfo["validata"]

        res = RequestUtil().send_request(method=methods, url=urls, params=datas)
        result = res.json()
        data = {"access_token": result["access_token"]}
        write_yaml("extract.yaml", data)

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/select_flag.yaml"))
    def test_select_flag(self, caseinfo):
        names = caseinfo["name"]
        methods = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]
        headers = caseinfo["request"]["headers"]
        datas = caseinfo["request"]["params"]
        datas["access_token"] = read_extract_yaml("extract.yaml", "access_token")
        validatas = caseinfo["validata"]

        res = RequestUtil().send_request(method="get", url=urls, params=datas)
        result = res.json()
        print(result, type(result))

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/edit_flag.yaml"))
    def test_edit_flag(self, caseinfo):
        names = caseinfo["name"]
        methods = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]
        headers = caseinfo["request"]["headers"]
        params = caseinfo["request"]["params"]
        params["access_token"] = read_extract_yaml("extract.yaml", "access_token")
        datas = caseinfo["request"]["json"]
        validatas = caseinfo["validata"]

        res = RequestUtil().send_request(method=methods, url=urls, json=datas, params=params)
        result = res.json()
        print(result, type(result))

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/delete_flag.yaml"))
    def test_delete_flag(self, caseinfo):
        methods = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]
        params = caseinfo["request"]["params"]
        params["access_token"] = read_extract_yaml("extract.yaml", "access_token")
        datas = caseinfo["request"]["json"]
        res = RequestUtil().send_request(method=methods, url=urls, json=datas, params=params)
        result = res.json()
        print(result, type(result))

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/file_upload.yaml"))
    def test_file_upload(self, caseinfo):
        method = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]
        params = caseinfo["request"]["params"]
        params["access_token"] = read_extract_yaml("extract.yaml", "access_token")
        datas = caseinfo["request"]["files"]
        datas["media"] = open(datas["media"], "rb")
        res = RequestUtil().send_request(method="post", url=urls, files=datas, params=params)
        result = res.json()
        print(result, type(result))


