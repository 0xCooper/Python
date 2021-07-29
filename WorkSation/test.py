import os
def file_list(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files
a=file_list("/media/makapaka/WorkStation/VsWorkstation/Python/virtualenv/django_workspace/static/")
print(a)