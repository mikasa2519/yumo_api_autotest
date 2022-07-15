import pytest

from commons.yaml_util import read_extract_yaml

if __name__ == '__main__':
    # pytest.main()

    url = "https://api.weixin.qq.com/cgi-bin/tags/get?access_token=${access_token}&abc=${abc}"
    for a in range(1, url.count("${")+1):
        if "${" and "}" in url:
            start_index = url.index("${")
            end_index = url.index("}", start_index)
            old_value = url[start_index:end_index + 1]
            new_value = read_extract_yaml("extract.yaml", old_value[2:-1])
            new_url = url.replace(old_value, new_value)
            url = new_url
            print(url)
