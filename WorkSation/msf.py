#-i https://pypi.tuna.tsinghua.edu.cn/simple
from pymsfrpc import msfrpc
ip = "127.0.0.1"
user = "msf"
passwd = "msf"
c = msfrpc.Client(ip,user,passwd)
output = c.get_version()
print(output[b"version"])
print(output[b"ruby"])