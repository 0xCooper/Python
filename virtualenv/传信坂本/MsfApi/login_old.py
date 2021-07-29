import msgpack
import http.client


class msf_login:
    token=""
#res req



    #配置
    options ={ 
        "login":["auth.login","Username","Password"],
        "auth":{
                "token_add":[ "auth.token_add", "<token>", "<NewToken>"],

                "token_list":[ "auth.token_list", "<token>"],
                "token_remove":[ "auth.token_remove", "<token>", "<TokenToBeRemoved>"],
        },

        "console":{
                "create":[ "console.create", "<token>"],
                "destory":[ "console.destroy", "<token>", "ConsoleID"],
                "write":[ "console.write", "<token>", "0", "wirte"],
                "read":[ "console.read", "<token>", "0"],
                "list":[ "console.list", "<token>"],
                "tab":[ "console.tabs", "<token>", "ConsoleID", "InputLine"],
                "session_kill":[ "console.session_kill", "<token>", "ConsoleID"],


        },
        "module":{

                "exploit":[ "module.exploits", "<token>" ],
                "auxiliary":[ "module.auxiliary", "<token>" ],
                "post":[ "module.post", "<token>" ],
                "encoders":[ "module.encoders", "<token>" ],
                "options":[ "module.options", "<token>", "ModuleType", "ModuleName" ],
                "info":[ "module.info", "<token>", "ModuleType", "ModuleName" ],
                

        },
        "session":{

                "list":[ "session.list", "<token>" ],
                "stop":[ "session.stop", "<token>", "SessionID" ],
                "read":[ "session.shell_read", "<token>", "SessionID", "ReadPointer" ],
                "write":[ "session.shell_write", "<token>", "SessionID", "id\n" ],
                

        },
        "meterpreter":{
                        "read":[ "session.meterpreter_read", "<token>", "SessionID"],
                        "write":[ "session.meterpreter_write", "<token>", "SessionID", "ps" ],
                        "tab":[ "session.meterpreter_tabs", "<token>", "SessionID", "InputLine"],
                }



    
    }

    def session_list(self):
        self.options['session']['list'][1]=self.token
        res=self.request(option=self.options['session']['list'])

        return res
        #字典中



    def meterpreter_write(self):
        self.options['meterpreter']['write'][1]=self.token
        res=self.request(option=self.options['metepreter']['write'])
        return res


    

    headers = {"Content-type" : "binary/message-pack"}

    
    def set_headers(self,value):
        self._headers = value
    
    def __init__(self,host,port,user,passwd):
        
        self.host=host
        self.port=port
        self.options["login"][1]=user
        self.options["login"][2]=passwd
        
    def connect(self):
        # 连接MSF RPC Socket
         self.req = http.client.HTTPConnection(self.host, self.port)
        
        #请求
    def request(self,option):
        #option为你的请求信息
        # 对参数进行序列化（编码）
        options = msgpack.packb(option)
        # 发送请求，序列化之后的数据包
        headers=self.headers
        self.req.request("POST","/api/1.0",body=options,headers=headers)          
        # 获取返回
        res = self.req.getresponse().read()
        # 对返回进行反序列户（解码）
        res = msgpack.unpackb(res)
        return res

    #获取临时的tokenls
    def get_tmptoken(self): 
        res=self.request(option=self.options['login'])
        self.token = res[b'token'].decode()
        return self.token

    def get_token(self):
        return self.token

    def console_create(self):
        self.options['console']['create'][1]=self.token
        res=self.request(option=self.options['console']['create'])
        return res


    def console_destory(self,id):
        self.options['console']['destory'][1]=self.token
        self.options['console']['destory'][2]=id
        res=self.request(option=self.options['console']['destory'])
        if res[b'result']==b'success':
            print("destroy success\n")
        else:
            print("destroy fail\n")
        return res


    def console_write(self,id,scanf):
        self.options['console']['write'][1]=self.token
        self.options['console']['write'][2]=id
        self.options['console']['write'][3]=scanf
        
        res=self.request(option=self.options['console']['write'])
        return res


    def console_read(self,id):
        self.options['console']['read'][1]=self.token
        self.options['console']['read'][2]=id
        res=self.request(option=self.options['console']['read'])
        return res

    def console_list(self):
        self.options['console']['list'][1]=self.token
        res=self.request(option=self.options['console']['list'])
        return res
        #返回一个字典 里面包含了console

    def token_add(self,newtoken):
        self.options['auth']['token_add'][1]=self.token
        self.options['auth']['token_add'][2]=newtoken
        res=self.request(option=self.options['auth']['token_add'])
        # self.token=newtoken
        return res
    
    def token_list(self):
        self.options['auth']['token_list'][1]=self.token
        res=self.request(option=self.options['auth']['token_list'])
        return res

    def token_set(self,mytoken):
        self.token=mytoken
        return 0
    
    def token_remove(self,removetoken):
        self.options['auth']['token_remove'][1]=self.token
        self.options['auth']['token_remove'][2]=removetoken
        res=self.request(option=self.options['auth']['token_remove'])
        return res
        #如何删除成功返回 { "result" => "success" }

    

    #销毁所有控制台
    def destory_all(self):
        dic=self.console_list()
        list=dic[b'consoles']
        for item in list:
            id=item[b'id'].decode()
            self.console_destory(id)
    
        #信息

    def info(self):
        print('''Metasplot Web System Api\n
                console_list() 显示所有控制台
                destory_all()  销毁所有控制台

            ''')

        return 0
    
        #开始  也就是登录过程
    def msf_start(self):
        self.connect()
        #临时token用户登录
        self.get_tmptoken()
  
  #结束
    def msf_end(self):
        self.destory_all()

    