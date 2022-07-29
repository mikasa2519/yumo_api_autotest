import pytest

from commons.yaml_util import clear_yaml


# 执行用例之前，先清空extract.yaml文件

@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    clear_yaml("extract.yaml")
