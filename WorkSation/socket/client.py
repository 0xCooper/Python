#!/usr/bin/python3
# 文件名：client.py

# 导入 socket、sys 模块
from os import sendfile
import socket
import sys
from tkinter.constants import TRUE

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname() 
# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
while TRUE:
    msg = s.recv(1024)
    print (msg.decode('utf-8'))
    
    data=""
    while data!="quit":
        data = input('>>').strip()
        if not data:
            break
        s.send(data.encode('utf-8')) #发送消息
    
    


s.close()

