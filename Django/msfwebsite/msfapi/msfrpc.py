# _*_ encoding:utf-8 _*_
# __author__ = "dr0op"
# python3

import msgpack
import http.client

HOST="127.0.0.1"
PORT="55553"
headers = {"Content-type" : "binary/message-pack"}






# 连接MSF RPC Socket
req = http.client.HTTPConnection(HOST, PORT)
options = ["auth.login","msf","msf"]
# 对参数进行序列化（编码）
options = msgpack.packb(options)
# 发送请求，序列化之后的数据包
req.request("POST","/api/1.0",body=options,headers=headers)
# 获取返回
res = req.getresponse().read()
# 对返回进行反序列户（解码）
res = msgpack.unpackb(res)
res = res[b'token'].decode()
print(res)
options2 = [ "console.create"]
options2.append(res)
print(options2)#发送的这个请求
options2=msgpack.packb(options2)
req.request("POST","/api/1.0",body=options2,headers=headers)
res2 = req.getresponse().read()
res2 = msgpack.unpackb(res2)
print(res2)#2创建一个终端


options3 = ["console.write"]
options3.append(res)
options3.append("0")
options3.append("search ms17_010\n")
print(options3)
options3 = msgpack.packb(options3)
req.request("POST","/api/1.0",body=options3,headers=headers)
res3 = req.getresponse().read()
res3 = msgpack.unpackb(res3)
print(res3)#创建一个终端


options5 =[ "console.read", "<token>", "0"]
options5[1]=res
print("+++++++++++++++++++++++++++")
options5 = msgpack.packb(options5)
req.request("POST","/api/1.0",body=options5,headers=headers)
res5 = req.getresponse().read()
res5 = msgpack.unpackb(res5)
print(res5[b'data'].decode())#创建一个终端
print("++++++++++++++++++++++++++++++")









#删除终端
for i in range(20):
    options4 = [ "console.destroy", "<token>", "ConsoleID"]
    options4[1]=res
    options4[2]=i+1
    options4 = msgpack.packb(options4)
    req.request("POST","/api/1.0",body=options4,headers=headers)
    res4 = req.getresponse().read()
    res4 = msgpack.unpackb(res4)
    print(res4)#创建一个终端
    print("%d delete"%(i+1))
