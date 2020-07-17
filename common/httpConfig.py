# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/6/19

import json
import requests

import sys
sys.path.append('../')
import readConfig as readConfig
import common.Log as Log

class HttpMethod():

	def __init__(self):
		self.log = Log.logger
		# self.headers = {}
		# self.params = {}
		# self.data = {}
		# self.url = None
		# self.files = {}


	# def set_headers(self, header):
	# 	self.headers = header
	#
	# def set_params(self, param):
	# 	self.params = param
	#
	# def set_data(self, data):
	# 	self.data = data
	#
	# def set_files(self, file):
	# 	self.files = file

	# defined http method
	def send_post(self, url, data=None, headers=None, files=None):
		try:
			result = requests.post(url=url, headers=headers,data=data, files=files).json()
			res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
			return res
		except Exception as e:
			self.log.error(e)

	def send_get(self, url, data=None, headers=None):
		try:
			result = requests.get(url=url, params=data, headers= headers).json()
			res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
			return res
		except Exception as e:
			self.log.error(e)

	def send_put(self, url, data=None, headers=None):
		try:
			result = requests.put(url=url, data=data, headers=headers)
			res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
			return res
		except Exception as e:
			self.log.error(e)

	def send_delete(self, url, data=None, headers=None):
		try:
			result = requests.delete(url=url, data=data, headers=headers)
			res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
			return res
		except Exception as e:
			self.log.error(e)

	def http_method(self, method, url, data=None, headers=None, files=None):
		result = None
		if method == 'post':
			result = self.send_post(url, data, headers, files=files)
		elif method == 'get':
			result = self.send_get(url, data, headers)
		elif method == 'put':
			result = self.send_get(url, data, headers)
		elif method == 'delete':
			result = self.send_get(url, data, headers)
		else:
			print("method值错误！！")
		return result

if __name__ == "__main__":

	result1 = HttpMethod().http_method('get', 'http://127.0.0.1:8888/login', 'name=xiaoming&pwd=111')
	print(result1)