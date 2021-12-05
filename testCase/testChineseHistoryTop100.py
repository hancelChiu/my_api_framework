# -*- coding: utf-8 -*-
# _author:"hancel"
# date:2021/12/4

import requests
import unittest
# from common.httpConfig import HttpMethod
import common.Log as Log


# import json


class TestAllWarTop100(unittest.TestCase):
    log = Log.logger
    url = "https://www.allhistory.com/api/m/topn/v1/n/list/byChannel?channel=3&language=cn"
    payload = {}
    headers = {
        'ax': 'f8b7c2cd6b87d712f4b;ba28f5a5d96c97ce1d0a359d8c3b29ac36238333;6858037b3c;458bba67d7dce08dc09665327f74af0037d5d189;1638407789612;1;'
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
            self.assertIsNotNone(res["data"]["list"])
            self.log.info("断言通过")
        except Exception as e:
            self.log.error(e)

    def testChineseHistoryTop100(self):
        self.passed()


if __name__ == "__main__":
    unittest.main()
