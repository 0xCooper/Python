from MsfApi.login import msf_login
# from login import msf_login
# from msfapi.login import msf_login

import time

#此库对获取的信息进一步处理

#get_tmptoken获取临时tokent
#get_token 获取当前token
def info():
    print("method 是一个对msfapi封装的方法库")
def print_token(obj):
    res=obj.get_token()
    print("传入token为  ",res,"\n")

#传入对象 对象为有这个token的链接 obj为有密码 ，有地址的的对象，他可以创建console，做各种事情
#不同对象的区别可能就是token不同 连接不同 状态不同（开没开始） 
#一个对象通过一个token进行通信

def get_console(obj):
    id_out=obj.console_create().get(b'id')
    if id_out is str:
        id_out=id_out.encode("utf8","ignore").decode("utf8","ignore")
    else:
        id_out=id_out.decode("utf8","ignore")
    return id_out

def get_idlist(obj):
    res=obj.console_list()
    
    #res是字典类型，里面有几个有id的控制台

def get_data(query,obj,id):

    write= obj.console_write(id,query)
    time.sleep(0.3)#等待前端反应完毕
    res=obj.console_read(id)
    data="error"
    try:
        data=res[b"data"].decode("utf8","ignore")
    except:
        print("出问题")
    
    return data

# def command(cmd,obj,id):
#     write= obj.console_write(id,query)
#     return write

def read_data(obj,id):
    res=obj.console_read(id)
    if res:
        if res[b'result']:
            return "读取失败，没有这个console"
        print(res)
        data=res[b'data'].decode("utf8","ignore")
        
        return data
    else:
        return "没有数据"

    
    

# def shell_read_data(obj,id):
#     res=obj.console_read(id)
#     data=res[b'data'].decode("utf8","ignore")
#     print(data[int(len(data)/2)])
#     return data

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
    if isinstance(data,list):    return list(map(convert,data.items()))
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
    res=obj.session_list()
    res=convert(res)
    print(res)
    return res

def get_joblist(obj):
    res=obj.job_list()  
    res=convert(res) 
    print(res)
    return res

def get_consolestatus(obj,id):
    res=get_consolelist(obj)
    for item in res:
        if id==item['id']:
            # print("prompt is :")
            # print( "          ",item['prompt'])
            return item['prompt']
    
    pass
 
def get_consoleid(obj):
    res=get_consolelist(obj)
    if res is None:
        print("no console establish")
    else:
        id_list=[]
        for item in res:
            id_list.append(str(item['id']))
        print(id_list)
        return id_list

# def get_sessionid(obj):
#     res=get_sessionlist(obj)


#     return 0
#     pass

def  get_m_data(obj,S_ID):
    res=obj.meterperter_read(S_ID)
    res=convert(res)
    print(res)
    return res









def attack_autu(obj):
    pass



# def test(query):
#     obj=msf_login( host, port, user, password)
#     query=""
#     #开始 连接并 获取token
#     token="helloworld"
#     id=9
#     #使用持久token通信
#     obj.connect()
#     obj.token_set(token)
#     query=query+"\n"
#     data= get_data(query,obj,id)
#     return data

def console_exploit(dic,write_cmd,id_input):

    obj=msf_login( dic['ip'], dic['port'], dic['user'], dic['password'])
    obj.connect()
    token=dic['token']
    obj.token_set(token)
    cmd1='use '+write_cmd['exploit_mod']+'\n'
    cmd2='set payload '+write_cmd['exploit_payload_type']+'\n'
    cmd3='set RHOST ' +write_cmd['exploit_rhost']+'\n'
    cmd4='set Lhost ' +dic['ip']+"\n"

    cmd_end="exploit \n"
    print(cmd1)
    print(cmd2)
    print(cmd3)
    print(cmd4)
    print("exploit执行完毕")
    data1=get_data(cmd1,obj,id_input)
    data2=get_data(cmd2,obj,id_input)
    data3=get_data(cmd3,obj,id_input)
    data4=get_data(cmd_end,obj,id_input)
    res_data=data1+data2+data3+data4
    return  res_data


    # id_input=get_console(obj)#创建一个console并获取id
    # prompt=get_consolestatus(obj,id_input)#获取console的光标
    # sessions=get_sessionlist(obj)
    # s_dic={}
    # s_dic['id']=id_input
    # s_dic['prompt']=prompt
    # s_dic['session_id']=sessions
    # return s_dic
    # pass



def console_use(dic,write,id_input):
    obj=msf_login( dic['ip'], dic['port'], dic['user'], dic['password'])
    obj.connect()
    token=dic['token']
    obj.token_set(token)
    write=write+"\n"
    data=get_data(write,obj,id_input)
    return data
    
def shell_use(dic,write,id_input):
    obj=msf_login( dic['ip'], dic['port'], dic['user'], dic['password'])
    obj.connect()
    token=dic['token']
    obj.token_set(token)
    #前面四部就是建立连接
    write=write+"\n"
    print("输入写入的是"+write)
    res_write=obj.shell_write(id_input,write)#res_write就你写了几个字符
    res_write2=obj.meterpreter_write(id_input,write)
    time.sleep(0.7)#等待前端反应完毕
    res=obj.shell_read(id_input)
    # res=read_data(obj,id_input)
    print("id是",id_input,res_write)
    # res=obj.meterpreter_read(id_input)
    print("res在这里",res)
    if res:
        res=res[b"data"].decode("utf8","ignore")

        return res
    else:
        return "error"
    pass

def session_info(dic):
    obj=msf_login( dic['ip'], dic['port'], dic['user'], dic['password'])
    obj.connect()
    token=dic['token']
    obj.token_set(token)
    data=get_sessionlist(obj)
    
    if data:
        sessions_info1=[]
        for k ,v in data.items():
            print("=============v:",v)
            session_status={}
            session_status['session_id']=k
            session_status['session_type']=v['type']
            session_status['session_host']=v['session_host']
            session_status['session_info']=v['info']
            session_status['session_uname']=v['username']
            session_status['session_via_exp']=v['via_exploit']
            session_status['session_via_pay']=v['via_payload']
            session_status['tunnel_local']=v['tunnel_local']
            session_status['tunnel_peer']=v['tunnel_peer']
            sessions_info1.append(session_status)
            
        return sessions_info1#返回的是一个列表 列表中有需要的session
    else:
        return "kong"
        #调用的时候做判断，kong就不继续


def login_start(dic):
    obj=msf_login( dic['ip'], dic['port'], dic['user'], dic['password'])
    obj.connect()
    print(obj.options['login'])
    obj.get_tmptoken()
    
    token=dic['token']
    change_longtoken(obj,token)
    return 0

    #单id
def console_start(dic):
    obj=msf_login( dic['ip'], dic['port'], dic['user'], dic['password'])
    obj.connect()
    
    token=dic['token']
    obj.token_set(token)
    id_input=get_console(obj)#创建一个console并获取id
    prompt=get_consolestatus(obj,id_input)
    # get_consolelist(obj)获取id信息
    sessions=get_sessionlist(obj)
    s_dic={}
    s_dic['id']=id_input
    s_dic['prompt']=prompt
    s_dic['session_id']=sessions
    return s_dic

def console_out(dic):
    obj=msf_login( dic['ip'], dic['port'], dic['user'], dic['password'])
    obj.connect()
    token=dic['token']
    obj.token_set(token)
    id_input=get_console(obj)
    obj.destory_all()
    

