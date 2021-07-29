from method import *
from login import msf_login
id =0
host="127.0.0.1"
port="55553"
user="msf"
password="msf"
info()
obj3=msf_login(host,port,user,password)
obj3.msf_start()



print_token(obj3)
