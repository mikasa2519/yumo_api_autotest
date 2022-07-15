import re

import pytest

from commons.request_util import RequestUtil
from commons.yaml_util import write_yaml, read_extract_yaml, read_testcase_yaml


class TestPhpWind:
    pass

    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/product_manager/phpwind_index.yaml"))
    # def test_index(self, caseinfo):
    #
    #     method = caseinfo["request"]["method"]
    #     urls = caseinfo["request"]["url"]
    #
    #     res = RequestUtil().send_request(method=method, url=urls)
    #     result = res.text
    #     data = {"csrf_token": re.search('name="csrf_token" value="(.*?)"', result).group(1)}
    #     write_yaml("extract.yaml", data)
    #
    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/product_manager/phpwind_login.yaml"))
    # def test_login(self, caseinfo):
    #
    #     methods = caseinfo["request"]["method"]
    #     urls = caseinfo["request"]["url"]
    #     header = caseinfo["request"]["headers"]
    #     datas = caseinfo["request"]["datas"]
    #     datas["csrf_token"] = read_extract_yaml("extract.yaml", "csrf_token")
    #
    #     res = RequestUtil().send_request(method=methods, url=urls, data=datas, headers=header)
    #     result = res.text
    #     print(result, type(result))
