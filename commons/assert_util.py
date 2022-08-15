import jsonpath


def assert_result(yq_result, sj_result, status_code):
    all_flag = 0
    print("预期结果: %s" % yq_result)
    print("实际结果: %s" % sj_result)
    for yq in yq_result:
        for key, value in yq.items():
            if key == "equals":
                print("这是一个相等断言")
                flag = equals_assert(value, sj_result, status_code)
                all_flag = all_flag + flag
            elif key == "contains":
                print("这是一个包含断言")
                flag = contains_assert(value, sj_result)
                all_flag = all_flag + flag
            else:
                print("框架不支持该断言方式")
    return all_flag


# 相等断言
def equals_assert(value, sj_result, status_code):
    flag = 0
    for assert_key, assert_value in value.items():
        if assert_key == "status_code":
            if assert_value != status_code:
                flag += 1
                print("equals断言失败：" + str(assert_key) + "不等于" + str(assert_value))
        else:
            key_lists = jsonpath.jsonpath(sj_result, '$..%s' % assert_key)
            if key_lists:
                if assert_value not in key_lists:
                    flag += 1
                    print("equals断言失败：" + str(assert_key) + "不等于" + str(assert_value))
            else:
                flag += 1
                print("equals断言失败：返回结果中没有" + str(assert_key))
    return flag


# 包含断言
def contains_assert(value, sj_result):
    flag = 0
    if str(value) not in str(sj_result):
        flag += 1
        print("contains断言失败：返回的结果中没有" + str(value))
    return flag
