from django.db import models

# Create your models here.
class Login(models.Model):
    ip=models.CharField(max_length=15)
    port = models.CharField(max_length=15)
    user = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    time=models.DateTimeField(auto_now_add=True)
    login_ip=models.CharField(max_length=15,default="127.0.0.1")
    def __str__(self):
        return self.user

class online(models.Model):
    ip=models.CharField(max_length=15)
    port = models.CharField(max_length=15)
    user = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    token =models.CharField(max_length=50,default="test")
    random =models.CharField(max_length=50,default="xxx")
    def __str__(self):
        return self.user

class msf_status(models.Model):
    #msf类的状态 可以让全局都能获得
    token=models.CharField(max_length=15)
    console_id=models.CharField(max_length=20)
    session_id=models.CharField(max_length=20)
    random_num =models.CharField(max_length=50,default="xxx")
    
class Act_info(models.Model):
    act_type = models.CharField(max_length=15)
    act_time = models.DateTimeField(auto_now_add=True)
    act_info = models.CharField(max_length=50)
    def __str__(self):
        return self.act_type
class console_status(models.Model):
    user=models.CharField(max_length=20)
    prompt=models.CharField(max_length=50,null=True)
    console_id=models.CharField(max_length=20)
    session_id=models.CharField(max_length=20)
    remark=models.CharField(max_length=20,default="console")
    # status_id=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.console_id
class Exploitinfo_save(models.Model):
    name=models.CharField(max_length=50)
    exploit_mod=models.CharField(max_length=50,null=True)
    exploit_rhost=models.CharField(max_length=20,null=True)
    exploit_payload_type=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name

class session_status(models.Model):
    # console_id=models.CharField(max_length=20)
    session_id=models.CharField(max_length=20)
    session_type=models.CharField(max_length=20)
    session_host=models.CharField(max_length=20,null=True)
    tunnel_local=models.CharField(max_length=20,null=True)
    tunnel_peer=models.CharField(max_length=20,null=True)
    session_uname=models.CharField(max_length=20,null=True)
    session_info=models.CharField(max_length=200,null=True)
    session_via_exp=models.CharField(max_length=50,null=True)
    session_via_pay=models.CharField(max_length=50,null=True)#payload
    def __str__(self):
        return self.id

