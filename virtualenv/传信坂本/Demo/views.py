from django.shortcuts import render,redirect,HttpResponse
from django.views import View 
from Demo.form import LoginForm,shellcode
from Demo.models import Login,Act_info,online,console_status,Exploitinfo_save,session_status
from django.http import FileResponse,Http404

from MsfApi.msfveonm import *
from MsfApi.file_act import *
from MsfApi.method import *

import string
import random
#随机生成密码


# Create your views here.

def Index(request):
    #前端post来的数据然后通过api执行后再传输回去
    if request.method =='GET':
        try:

            content=request.get_signed_cookie("content",salt="pass")
            uname=request.COOKIES.get('uname')
            port=request.COOKIES.get('port')
            random_num=request.COOKIES.get('random_num')
            if content:
                info=online.objects.filter(user=uname).filter(port=port).filter(random=random_num).values('ip','port','user','password','token') 
                info=info[0]
                #创建console 保存状态
                # s_dic=console_start(info)
                # sta=console_status(user=uname,prompt=s_dic['prompt'],console_id=s_dic['id'],session_id=s_dic['session_id'])
                # sta.save()
                res_content={}
                res_content['uname']=uname
                return render(request,'index.html',res_content)
            else:
                return HttpResponse("出错了")
        except Exception as result:
            print('index检测出异常{}'.format(result))
            # return HttpResponse("nothing")
            return redirect(to='login')
        

class LoginView(View):
    def get(self,request):
        # form=LoginForm
        # content={}
        # content['form']=form
        # return render(request,'login.html',content)
        return render(request,'login.html')

    def post(self,request):
        # form=LoginForm(request.POST)
        try:
            print("test")
        except Exception as result:
            print('检测出异常{}'.format(result))
            
            return HttpResponse("发生错误")
        
        ip=request.POST.get('ip')
        port=request.POST.get('port')
        user=request.POST.get('username')
        password=request.POST.get('password')
        # if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        #     ip =  request.META.get('HTTP_X_FORWARDED_FOR')
        # else:
        #     ip = request.META.get['REMOTE_ADDR']
        login_ip=request.META.get('REMOTE_ADDR')
        l=Login(ip=ip,port=port,user=user,password=password,login_ip=login_ip)
        l.save()
        
        uname=user
        #随机数相当于token 并存入online数据库
        
        random_num="".join(random.choices(string.ascii_letters+string.digits,k=random.randint(8,19)))
        print(random_num)
        login_status=online(ip=ip,port=port,user=user,password=password,random=random_num)
        login_status.save()
        info=online.objects.filter(user=user).filter(port=port).filter(ip=ip).filter(random=random_num).values('ip','port','user','password','token') 
        info=info[0]



        # print(info)
        # login_start(info)
        try:
            print(info)
            login_start(info)
        except Exception as result:
            print('login_1检测出异常{}'.format(result))
            online.objects.filter(user=uname).delete()
            return HttpResponse("Metasploit连接不上,请检查错误")
        #创建console 保存状态

        s_dic={}
        s_dic=console_start(info)
        # random_num2="".join(random.choices(string.ascii_letters+string.digits,k=random.randint(8,19)))
        sta=console_status(user=uname,prompt=s_dic['prompt'],console_id=s_dic['id'],session_id=s_dic['session_id'])
        sta.save()
        res=redirect(to='index')
        #设置cookie
        res.set_signed_cookie("content",user+ip,"pass")
        res.set_cookie('uname',uname)
        res.set_cookie('port',port)
        res.set_cookie('random_num',random_num)
        return res
        # except Exception as result:
        #     print('login检测出异常{}'.format(result))
            
        #     return HttpResponse("login发生错误")
        #     # return redirect(to='index')
def file_trojan(request):
    host = request.GET.get('lhost')
    port = request.GET.get('lport')
    name=request.GET.get('name')
    env=request.GET.get('env')
    
    file_type=judge_env(env)
    status=Trojan(host,port,name,env)
    info=host+":"+port+"  文件名: "+name+" 类型: "+file_type
    act=Act_info(act_type="payload生成",act_info=info)
    act.save()
    if status==1:
        return HttpResponse("下载出错了")
    if status=="input error":
        return HttpResponse("存在错误的输入")
    else:
        return redirect(to='payload')
def upload_file(request):
    if request.method == 'POST':
        obj = request.FILES.get('upload_file')  
        file_path=os.path.join('static','upload', '', obj.name) 
        
        with open(file_path, 'wb+') as destination:
            for chunk in obj.chunks():
                destination.write(chunk)
        return  HttpResponse('OK')
    return render(request, 'upload.html')
def Data_clear(request):
    try:
        content=request.get_signed_cookie("content",salt="pass")
        if content:
            id= request.GET.get('id')
            if id=="all":
                Login.objects.all().delete()
                return redirect(to='history')
            else:    
                
                Login.objects.filter(id=id).delete()
                return redirect(to='history')
    except Exception as result:
        print('检测出异常{}'.format(result))
        return HttpResponse("发生错误")




def Actinfo__clear(request):
    try:
        content=request.get_signed_cookie("content",salt="pass")
        if content:
            id= request.GET.get('id')
            if id=="all":
                Act_info.objects.all().delete()
                return redirect(to='history')
            else:
                Act_info.objects.filter(id=id).delete()
                return redirect(to='history')
        else:
            pass
    except Exception as result:
        print('检测出异常{}'.format(result))
        return HttpResponse("发生错误")
        # return redirect(to='index')

def logout(request):
    if request.method=="GET":
        uname=request.COOKIES.get('uname')
        random_num=request.COOKIES.get('ramdom_num')
        if random_num:
            info=online.objects.filter(random=random_num).values('ip','port','user','password','token') 
            info=info[0]
            console_out(info)
        else:
            info=online.objects.filter(user=uname).values('ip','port','user','password','token') 
            info=info[0]
            console_out(info)
        
        #删除数据库中在线信息与console信息
        online.objects.filter(user=uname).delete()
        console_status.objects.filter(user=uname).delete()
        
        response=redirect(to="login")
        response.delete_cookie("content")
        response.delete_cookie("uname")
        response.delete_cookie('random_num')
        return response



def payload(request):
    if request.method== 'GET':
        try:
            content=request.get_signed_cookie("content",salt="pass")
            if content:
                content_res={}
                file_path='static/files/'
                # %s.%s'%(name,file_type)
                file_name=names_dict(file_path)
                
                content_res['filename']=file_name
                return render(request, 'payload.html',content_res)
        except:
            print("payload出错")
            return redirect(to='index')

def history(request):
    if request.method== 'GET':
        try:
            content=request.get_signed_cookie("content",salt="pass")
            if content:
                content_res={}
                user_list = Login.objects.all()
                content_res['data']=user_list
                act_list =Act_info.objects.all()
                content_res['act']=act_list
                return render(request,'history.html',content_res)
                # return render(request, 'history.html')
        except Exception as result:
            print('检测出异常{}'.format(result))
            # return HttpResponse("nothing")
            return redirect(to='index')

def payload_del(request):
    try:
        content=request.get_signed_cookie("content",salt="pass")
        if content:
            if request.method== 'GET':
                filename = request.GET.get('filename')
                file_path='static/files/'
                filename=file_path+filename
                os.remove(filename)
                return redirect(to='payload')
    except Exception as result:
            print('检测出异常{}'.format(result))
            # return HttpResponse("发生错误")
            return redirect(to='payload')

def payload_download(request):
    try:
        content=request.get_signed_cookie("content",salt="pass")
        if content:
            if request.method== 'GET':
                filename = request.GET.get('filename')
                file_path='static/files/%s'%(filename)
                try:
                    response = FileResponse(open(file_path, 'rb'))
                    response['content_type'] = "application/octet-stream"
                    response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                    return response
                except Exception as result:
                    print('检测出异常{}'.format(result))
                    return HttpResponse("下载出错了")
    except Exception as result:
            print('检测出异常{}'.format(result))
            # return HttpResponse("nothing")
            return redirect(to='payload')
def payload_upload(request):
    random_num=request.COOKIES.get('random_num')
    if request.method== 'GET':
        return redirect(to='login')
    if random_num:
        if request.method== 'POST':
            obj = request.FILES.get('upload_file')
            if not obj: 
                return  redirect(to='payload') 
            file_path=os.path.join('static','files', '', obj.name) 
            
            with open(file_path, 'wb+') as destination:
                for chunk in obj.chunks():
                    destination.write(chunk)
            return  redirect(to='payload')         
    else:
        return redirect(to='login')





def console_get(request):
    try:
        content=request.get_signed_cookie("content",salt="pass")
        uname=request.COOKIES.get('uname')
        port=request.COOKIES.get('port')
        random_num=request.COOKIES.get('random_num')
    except Exception as result:
            print('检测出异常{}'.format(result))
            # return HttpResponse("nothing")
            return HttpResponse("出问题了ok")
    finally:
        if content:
            if request.method=='POST':
                usr_input=request.POST.get('input')
                result="你的输入： "+usr_input
                if uname:
                    # obj=online.objects.filter(user=uname)
                    # token=online.objects.filter(user=uname).values('token') 
                    ip=online.objects.filter(random=random_num).values('ip','port','user','password','token') 
                    ip=ip[0]
                    print(ip)
                    id_input=console_status.objects.filter(user=uname).filter(remark="console").values('console_id').first()
                    print(id_input)
                    res_data=console_use(ip,usr_input,id_input['console_id'])
                    if res_data=="error":
                        res_data="出现了错误，没有数据返回，可以尝试退出重新登录"
                    res_data=res_data.replace("\n", "<br>")
                    print(res_data)
                    
                    result=result+"<br>"+res_data

                    act=Act_info(act_type="控制台写入",act_info=usr_input)
                    act.save()
                return  HttpResponse(result)
                

def exploit(request):
    content=request.get_signed_cookie("content",salt="pass")
    uname=request.COOKIES.get('uname')
    port=request.COOKIES.get('port')
    random_num=request.COOKIES.get('random_num')
    if request.method== 'GET':
        random_num=request.COOKIES.get('random_num')
        if random_num:
            exploit_info =Exploitinfo_save.objects.all()
            content_res={}
            content_res['attack_save']=exploit_info
            # content_res['attack_save']=Act_info.objects.all()
            return render(request, 'exploit.html',content_res)
        else:
            return redirect(to='login')
    if request.method== 'POST':
        save_name=request.POST.get('save_name')
        exploit_mod=request.POST.get('exploit_mod')
        payload_type=request.POST.get('payload_type')
        rhost=request.POST.get('rhost')
        cmd={}
        cmd['exploit_mod']=exploit_mod
        cmd['exploit_payload_type']=payload_type
        cmd['exploit_rhost']=rhost
        info=online.objects.filter(random=random_num).values('ip','port','user','password','token')
        info=info[0]
        console_start(info)
        s_dic=console_start(info)
        
        # random_num2="".join(random.choices(string.ascii_letters+string.digits,k=random.randint(8,19)))
        sta=console_status(user=uname,prompt=s_dic['prompt'],console_id=s_dic['id'],session_id=s_dic['session_id'],remark="exploit")
        sta.save()
        #fun_data是执行了那一堆东西，返回的东西
        fun_data=console_exploit(info,cmd,s_dic['id'])
        print(fun_data)
        res_data=save_name+" 执行完毕"+"请查看session情况"
        return HttpResponse(res_data)
        #console没有销毁
def exploit_button(request):
    if request.method== 'GET':
            random_num=request.COOKIES.get('random_num')
            if random_num:
                content_res={}
                # content_res['attack_save']=Act_info.objects.all()
                return render(request, 'exploit.html',content_res)
            else:
                return redirect(to='login')
    if request.method== 'POST':
        exploit_id=request.POST.get('exploit_id')
        print(exploit_id)
        return HttpResponse("完成执行")
        
def exploit_save(request):
    if request.method== 'GET':
            random_num=request.COOKIES.get('random_num')
            if random_num:
                content_res={}
                # content_res['attack_save']=Act_info.objects.all()
                return render(request, 'exploit.html',content_res)
            else:
                return redirect(to='login')
    if request.method== 'POST':
        save_name=request.POST.get('save_name')
        exploit_mod=request.POST.get('exploit_mod')
        payload_type=request.POST.get('payload_type')
        rhost=request.POST.get('rhost')
        print(save_name)
        exploit_info=Exploitinfo_save(exploit_mod=exploit_mod,exploit_rhost=rhost,exploit_payload_type=payload_type,name=save_name)
        exploit_info.save()
        print(save_name)
        return redirect(to='exploit')



def session(request):
    if request.method== 'GET':
        random_num=request.COOKIES.get('random_num')
        if random_num:
            
            
            content_res={}
            info=online.objects.filter(random=random_num).values('ip','port','user','password','token') 
            info=info[0]
            
            res_info=session_info(info)
            print(res_info)
            session_status.objects.all().delete()
            if res_info=='kong':
                return render(request, 'session.html',content_res)
            for i in res_info:
                info_save=session_status(session_id=i['session_id'],session_type=i['session_type'],session_host=i['session_host'],session_info=i['session_info'],session_uname=i['session_uname'],tunnel_local=i['tunnel_local'],session_via_exp=i['session_via_exp'],session_via_pay=i['session_via_pay'],tunnel_peer=i['tunnel_peer'])
                info_save.save()
                print("=========数据save进入数据库=========")
            content_res['sessions'] =session_status.objects.all()
            return render(request, 'session.html',content_res)
        else:
            return redirect(to='login')



def shell_get(request):
    try:
        content=request.get_signed_cookie("content",salt="pass")
        uname=request.COOKIES.get('uname')
        port=request.COOKIES.get('port')
        random_num=request.COOKIES.get('random_num')
    except Exception as result:
            print('检测出异常{}'.format(result))
            # return HttpResponse("nothing")
            return HttpResponse("出问题了ok")
    finally:
        if content:
            if request.method=='POST':
                usr_input=request.POST.get('input')
                id_choice=request.POST.get('session_id')
                result="你的输入： "+usr_input
                if uname:
                    # obj=online.objects.filter(user=uname)
                    # token=online.objects.filter(user=uname).values('token') 
                    info=online.objects.filter(random=random_num).values('ip','port','user','password','token') 
                    info=info[0]
                    # res_data=console_use(ip,usr_input,id_input['console_id'])
                    res_data=shell_use(info,usr_input,id_choice)
                    if not res_data:
                        res_data="没有返回值，读取不了"
                    if res_data=="error":
                        res_data="出现了错误，没有数据返回，可以尝试退出重新登录"
                    res_data=res_data.replace("\n", "<br>")
                    # print(res_data)
                    
                    result=result+"<br>"+res_data
                    act_info="id:"+id_choice+"输入"+usr_input
                    act=Act_info(act_type="shell利用",act_info=act_info)
                    act.save()
                return  HttpResponse(result)







def file_del(request):
    pass
def file_add(request):
    pass
def msf_search(request):
    pass
def msf_status(request):
    pass

