import os

import yaml


# 获得项目根路径
def get_object_path():
    print(os.getcwd())
    return os.getcwd()


# 写入yaml文件
def write_yaml(yaml_path, data):
    with open(get_object_path() + "/" + yaml_path, mode="a", encoding="utf-8") as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 清空yaml文件
def clear_yaml(yaml_path):
    with open(get_object_path() + "/" + yaml_path, mode="w", encoding="utf-8") as f:
        f.truncate()


# 读取测试用例yaml文件
def read_testcase_yaml(yaml_path):
    with open(get_object_path() + "/" + yaml_path, mode="r", encoding="utf-8", ) as f:
        result = yaml.load(stream=f, Loader=yaml.FullLoader)
        return result

get_object_path()