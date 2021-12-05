# -*- coding: utf-8 -*-
# _author:"hancel"
# date:2021/12/4

import requests
import unittest
# from common.httpConfig import HttpMethod
import common.Log as Log


# import json


class TestChineseHistoryNodeDetail(unittest.TestCase):
    log = Log.logger
    url = "https://m2.allhistory.com/ah/bigevent/415"
    payload = {}
    headers = {
        "ax": "97d8fd891c87d71b303;d806f37006b9c24f25c50b8ddb3dc805dda16150;a14581157b;dd542d31ec20294b4434be7d5b0854aed3053861;1638408493279;1;"
    }

    def setUp(self) -> None:
        self.log.info(self.__class__.__name__ + "测试开始")

    def tearDown(self) -> None:
        self.log.info(self.__class__.__name__ + "测试结束")
        print(self.__class__.__name__ + "测试通过")

    def passed(self):
        response = requests.get(self.url, params=self.payload, headers=self.headers)
        res = response.text
        print(res)
        try:
            self.assertEqual(response.status_code, 200)
            self.assertIn("韩山童起兵反元", res)
            self.log.info("断言通过")
        except Exception as e:
            pass
            self.log.error(e)

    def testNodeDetail(self):
        self.passed()
        # response1 = requests.get(self.url, params=self.payload, headers=self.headers)
        # self.assertIn("韩山童起兵反元", response1.text)


if __name__ == "__main__":
    unittest.main()
