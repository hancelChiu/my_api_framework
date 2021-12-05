# -*- coding: utf-8 -*-

""" 
@Author  : qiuhanqiu
@Time    : 2021/12/5 18:01
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime

import sys

sys.path.append('../')
import readConfig as readConfig

sys.path.append('F:\Python\my_api_framework\common')
import Log as Log

"""
服务器名称: smtp.office365.com
端口: 587
加密方法: STARTTLS
"""
localReadConfig = readConfig.ReadConfig()
log_path = Log.log_path
log = Log.logger
# host = localReadConfig.get_email('mail_host')
host = "smtp.office365.com"
# user = localReadConfig.get_email('mail_user')
user = "qiuhanqiu@outlook.com"
# password = localReadConfig.get_email('mail_pass')
password = "qiu06040710"
# port = localReadConfig.get_email('mail_port')
port = 587
# sender = localReadConfig.get_email('sender')
sender = "qiuhanqiu@outlook.com"
title = localReadConfig.get_email('subject')
content = localReadConfig.get_email('content')
# mail_path = os.path.join(log_path, u"report.html")  # 获取测试报告路径
mail_path = 'F:\\Python\\my_api_framework\\result\\20211205175617\\report.html'

# defined email subject
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
subject = title + "" + date
value = localReadConfig.get_email('receiver')
receiver = []
print(subject)
print(content)
# get receiver list
for n in str(value).split(","):
    receiver.append(n)


class send_email():
    def sendoutlook(self):

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = ';'.join(receiver)
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText(content, 'plain', 'utf-8'))
        att = MIMEText(open(mail_path, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="report_test.html"'
        message.attach(att)
        try:
            smtp = smtplib.SMTP()  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
            smtp.connect(host, port)
            # 登录
            smtp.ehlo()  # 向邮箱发送SMTP 'ehlo' 命令
            smtp.starttls()
            smtp.login(user, password)
            smtp.sendmail(sender, receiver, message.as_string())
            print("邮件发送成功！！！")
            log.info("邮件发送成功！！！")
            smtp.quit()
        except Exception as e:
            log.error(str(e))


if __name__ == '__main__':
    email = send_email()
    email.sendoutlook()
