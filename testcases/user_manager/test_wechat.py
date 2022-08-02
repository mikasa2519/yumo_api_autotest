import random
import re

import pytest

from commons.request_util import RequestUtil
from commons.yaml_util import read_testcase_yaml
from hot_loads.debug_talk import DebugTalk


class TestApi:

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/get_token.yaml"))
    def test_get_token(self, caseinfo):
        RequestUtil(DebugTalk()).standard_yaml_testcases(caseinfo)

    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/select_flag.yaml"))
    # def test_select_flag(self, caseinfo):
    #     RequestUtil(DebugTalk()).standard_yaml_testcases(caseinfo)
    #
    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/create_flag.yaml"))
    # def test_create_flag(self, caseinfo):
    #     RequestUtil(DebugTalk()).standard_yaml_testcases(caseinfo)
    #
    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/edit_flag.yaml"))
    # def test_edit_flag(self, caseinfo):
    #     RequestUtil(DebugTalk()).standard_yaml_testcases(caseinfo)
    #
    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/delete_flag.yaml"))
    # def test_delete_flag(self, caseinfo):
    #     RequestUtil(DebugTalk()).standard_yaml_testcases(caseinfo)
    #
    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/file_upload.yaml"))
    # def test_file_upload(self, caseinfo):
    #     RequestUtil(DebugTalk()).standard_yaml_testcases(caseinfo)


