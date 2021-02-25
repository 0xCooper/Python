'''
Descripttion: 发送邮箱
version: 
Author: myc
Date: 2021-02-25 08:52:23
'''
#!/usr/bin/python3
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

import  time
 
my_sender='3096780454@qq.com'    # 发件人邮箱账号
my_pass = 'usgrqeuvedkhdfhc'              # 发件人邮箱密码
my_user= '1306588647@qq.com'      # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
    try:
        msg=MIMEText('沙比国海在干嘛','plain','utf-8')
        msg['From']=formataddr(["Fromgrandfa",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="爷爷发来的邮箱"                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # SMTP端口是25 QQ 邮箱 SMTP 服务器地址：smtp.qq.com，ssl 端口：465
        server.login(my_sender, my_pass)            # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret

for i in range(10): 
    ret=mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
