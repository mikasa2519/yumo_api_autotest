import requests


class RequestUtil:
    # 初始化session对象
    sess = requests.session()

    def send_request(self, method, url, **kwargs):
        res = RequestUtil.sess.request(method, url, **kwargs)
        return res
