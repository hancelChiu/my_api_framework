# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/6/19

import os
from xlrd import open_workbook
import getpathInfo

path = getpathInfo.get_path()

class readExcel():
	def get_xls(self, xls_name, sheet_name):
		cls =[]
		# 获取用例文件路径
		excel_path = os.path.join(path, 'data', xls_name)
		file = open_workbook(excel_path)
		sheet = file.sheet_by_name(sheet_name)
		# 获取这个sheet内容行数
		nrows = sheet.nrows
		for i in range(nrows):
			if sheet.row_values(i)[0] != 'case_name':
				cls.append(sheet.row_values(i))
		return cls

if __name__ == "__main__":
	print(readExcel().get_xls('TestCase.xlsx', 'login'))


