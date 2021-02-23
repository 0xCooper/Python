'''
Descripttion: 目录遍历
version: 
Author: myc
Date: 2021-02-22 23:07:28
'''
import os 

g = os.walk(r"./")  

for path,dir_list,file_list in g:  
    for file_name in file_list:  
        print(os.path.join(path, file_name) )