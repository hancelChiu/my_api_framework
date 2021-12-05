# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/6/19

import os
import configparser
import codecs
import getpathInfo

path = getpathInfo.get_path()
config_path = os.path.join(path, 'config/config.ini')


class ReadConfig():

	def __init__(self):
		with open(config_path, 'r') as f:
			data = f.read()
		# remove BOM
			if data[:3] == codecs.BOM_UTF8:
				data = data[3:]
				file = codecs.open(config_path ,'w')
				file.write(data)
				file.close()
		self.cf = config = configparser.ConfigParser()
		self.cf.read(config_path, encoding='utf-8')

	def get_base_url(self):
		protocol = self.cf.get("HTTP", "protocol")

    host = self.cf.get("HTTP", "host")
		port = self.cf.get("HTTP", "port")


base_url = protocol + '://' + host + ':' + port
# base_url = protocol + '://' + host
		return base_url


	def get_http(self, name):
		value = self.cf.get('HTTP', name)
		return value

	def get_email(self, name):
		value = self.cf.get('EMAIL', name)
		return value


if __name__ == '__main__':
	print(ReadConfig().get_base_url())