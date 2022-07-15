一、规范YAML测试用例的编写：
    1.在YAML用例中，必须包含一级关键字：name request validate
    2.request下方必须包含二级关键字：method，url

二、关于接口关联
    1.保存中间变量
        1).此框架仅支持正则表达式提取以及Jsonpath提取，并且表达式匹配的值只能有一个
        2).提取的实例如下：extract是一级关键字
         extract:
            access_token1: '"access_token":"(.*?)"'
            access_token2: $.access_token
            expires_in: $.expires_in

    2.使用中间变量