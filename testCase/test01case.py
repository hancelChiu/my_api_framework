# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/6/22

import json
import unittest
import sys
sys.path.append('../')
from common.httpConfig import HttpMethod
import paramunittest
import urllib.parse
import readExcel
import readConfig as readConfig


url = readConfig.ReadConfig().get_base_url()
login_xls = readExcel.readExcel().get_xls('TestCase.xlsx', 'login')

@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
	def setParameters(self, case_name,path, query, method):
		self.case_name = str(case_name)
		self.path = str(path)
		self.query = str(query)
		self.method = str(method)
		self.url= url + self.path + "?"

	def description(self):
		self.case_name

	def setUp(self):
		print(self.case_name + "测试开始前准备")

	def test01case(self):
		self.checkResult()

	def tearDown(self):
		print("测试结束，输出log完结\n\n")

	def checkResult(self):
		url1 = "http://www.xxx.com/login?"
		new_url = url1 + self.query
		data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
		info = HttpMethod().http_method(self.method, self.url, data=data1)
		ss = json.loads(info)
		if self.case_name == 'login':
			self.assertEqual(ss['code'], 200)
		if self.case_name == 'login_error':
			self.assertEqual(ss['code'], -1)
		if self.case_name == 'login_null':
			self.assertEqual(ss['code'], 10001)

if __name__ == "__main__":
	unittest.main()