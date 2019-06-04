import unittest
from demo2 import app
import json
class LoginTestCase(unittest.TestCase):
    # 传入参数不足,返回errcode = -1
    def test_empty_username_password(self):
        app.test_client().post('/login',data={})
        resp_data = response.data
        json_dict = json.loads
        print(resp_data)
        