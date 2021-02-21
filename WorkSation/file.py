#coding = utf-8

import os  as win
uri ="b.txt" # 文件路径
with open(uri, 'a',encoding='utf-8') as f:
    f.write("Python english\n")
    f.write("中文输入")


# 删除文件模块
# rm = "del "+uri
# win.system(rm)
