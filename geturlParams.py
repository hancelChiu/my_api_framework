# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/6/22

import readConfig as readConfig

readconfig = readConfig.ReadConfig()

class geturlParams():
	def get_url(self):
		new_url = readconfig.get_http('protocol')+ "://" +readconfig.get_http('host') + ":"+ readconfig.get_http('port') + '/login' + '?'
		return new_url

if __name__ == "__main__":
	print(geturlParams().get_url())