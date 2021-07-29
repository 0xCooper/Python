import os


def print_list(list_a):
    for i in list_a:
        print(i)

def file_list(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files
        
def names_dict(file_dir):
    file_name=file_list(file_dir)
    j=0
    filename_list=[]
    for i in file_name:
        dict_name={}
        j+=1
        dict_name['id']=j
        dict_name['name']=i
        # print(dict_name)
        filename_list.append(dict_name)
    return filename_list
    
def file_del():
    pass


def file_add():
    pass

def file_rename():
    pass



