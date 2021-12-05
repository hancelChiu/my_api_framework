# -*- coding: utf-8 -*-
# _author:"hancel"
# date:2021/12/4

import requests
import unittest
from common.httpConfig import HttpMethod
import common.Log as Log
import json


class TestDefaultPeriod(unittest.TestCase):
    log = Log.logger
    url = "https://www.allhistory.com/api/m/bigEvent/v1/n/defaultPeriod/cn?eventId=0&language=cn"
    payload = {}
    headers = {
        'ax': '284c83cd6b87d71b175;10e3d776c25b601c947d38cda0b597eff939a31d;bacd7a343d;371b9d7ba882fb91edc412a122a350c035798912;1638407789624;1;'
    }

    def setUp(self) -> None:
        self.log.info(self.__class__.__name__ + "测试开始")

    def tearDown(self) -> None:
        self.log.info(self.__class__.__name__ + "测试结束")
        print(self.__class__.__name__ + "测试通过")

    def passed(self):
        response = requests.get(url=self.url, params=self.payload, headers=self.headers)
        res = response.json()
        print(res)  # 打印内容会输出到报告
        try:
            self.assertEqual(res["code"], 200)
            self.assertEqual(res["message"], "成功")
            self.assertIsNotNone(res["data"]["periods"])
            self.log.info("断言通过")
        except Exception as e:
            self.log.error(e)

    def testDefaultPeriod(self):
        self.passed()
        # response1 = requests.get(self.url, params=self.payload, headers=self.headers)
        # print(response1.text)


if __name__ == "__main__":
    unittest.main()
