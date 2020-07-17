# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/6/19

import flask
import json
from flask import request

# 创建一个服务，把当前这个python文件当做一个服务

server = flask.Flask(__name__)
# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
@server.route('/login', methods=['get', 'post'])
def login():
	# 获取通过url请求传参的数据
	username = request.values.get('name')
	pwd = request.values.get('pwd')
	# 判断用户名、密码都不为空
	if username and pwd :
		if username == 'xiaoming' and pwd == '111':
			res = {'code':200, 'message':'登录成功'}
			return json.dumps(res, ensure_ascii=False)
		else:
			res = {'code':-1, 'message':'账号密码错误'}
			return json.dumps(res, ensure_ascii=False)
	else:
		res = {'code': 10001, 'message':'参数不能为空！'}
		return json.dumps(res, ensure_ascii=False)

if __name__ == "__main__":
	server.run(debug=True, port=8888, host = '127.0.0.1')
