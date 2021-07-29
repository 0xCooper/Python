from login import msf_login
import time

#这里用一个类来开启console
#一个对象代表一个console
class usemsf:
    host="127.0.0.1"
    port="55552"
    user="msf"
    password="msf"
    
    def config_set(self,set):
        #set为传入的参数,暂定传入字典
        self.host=set['host']
        self.port=set['port']
        self.user=set['user']
        self.password=set['password']        
    def __init__(self):
        self.obj=msf_login(self.host,self.port,self.user,self.passwd)
        self.obj.msf_start()

    def get_data(self,query):
        
        id=obj.console_create().get(b'id').decode()
        print(id,end="\n")
        write= obj.console_write(id,query)
        res=obj.console_read(id)
        data=res[b"data"].decode()
        
        print(data)
        return data

    def end_console(self):
        obj.msf_end()   
        

    if __name__ == "__main__":
        get_data("search cve\n")





    

            