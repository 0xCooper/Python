

django 
    pip install Django==3.1
djangorestframework==3.12.4
    pip install djangorestframework  

换源 ：-i   https：//pypi.douban.com/simple/

session list 


登录流程
    实例化一个登录对象
    对象
        先用临时token去获取持久的token
        再通过持久token去传递回话

        get_token()可以返回当前token的值

        加载rpc
        msf5 > load msgrpc ServerHost=127.0.0.1 ServerPort=55553 User='msf' Pass='msf'