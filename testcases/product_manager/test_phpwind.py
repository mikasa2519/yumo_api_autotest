import pytest

from commons.request_util import RequestUtil
from commons.yaml_util import read_testcase_yaml


class TestPhpWind:

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/product_manager/phpwind_index.yaml"))
    def test_index(self, caseinfo):
        RequestUtil().standard_yaml_testcases(caseinfo)

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/product_manager/phpwind_login.yaml"))
    def test_login(self, caseinfo):
        RequestUtil().standard_yaml_testcases(caseinfo)
