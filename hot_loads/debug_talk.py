import os
import random

import yaml


class DebugTalk:

    # 获取随机数
    def get_random(self, min, max):
        return random.randint(int(min), int(max))

    # 读取extract.yaml文件
    def read_extract_yaml(self, key):
        with open(os.getcwd() + "/extract.yaml", mode="r", encoding="utf-8") as f:
            result = yaml.load(stream=f, Loader=yaml.FullLoader)
            return result[key]

