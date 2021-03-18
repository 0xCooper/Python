#!/bin/bash
# 作用：方便在控制台对内网穿透软件ngrok控制
a="http"
b="https"
c="tcp"
d="all"
if [ $1 == $a  ]
then
    echo "开启了http内网穿透服务"
    /windows/E/Tools/Nettools/ngrok-free/linux_amd64/ngrok -log=/.trash/ngroklog/ngrok.log -config /windows/E/Tools/Nettools/ngrok-free/linux_amd64/ngrok.conf start httptun
elif [ $1 == $b ]
then
    echo "开启了https内网穿透服务"
   /windows/E/Tools/Nettools/ngrok-free/linux_amd64/ngrok -log=/.trash/ngroklog/ngrok.log -config /windows/E/Tools/Nettools/ngrok-free/linux_amd64/ngrok.conf start httpstun 
#    echo "a 大于 b"
elif [ $1 == $c ]
then
    echo "开启了tcp内网穿透服务"
    /windows/E/Tools/Nettools/ngrok-free/linux_amd64/ngrok -log=/.trash/ngroklog/ngrok.log -config /windows/E/Tools/Nettools/ngrok-free/linux_amd64/ngrok.conf start tcptun
elif [ $1 == $d]
then
    echo "开启了http https tcp内网穿透服务"
    /windows/E/Tools/Nettools/ngrok-free/linux_amd64/ngrok -log=/.trash/ngroklog/ngrok.log -config /windows/E/Tools/Nettools/ngrok-free/linux_amd64/ngrok.conf start httptun httpstun 
else
   echo "没有符合的条件"
fi

