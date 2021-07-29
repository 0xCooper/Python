"""django_workspace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Demo.views import LoginView ,Index,file_trojan,Data_clear,upload_file,payload,logout,history,payload_del,payload_download,console_get,Actinfo__clear,exploit,session
from Demo.views import exploit_button,exploit_save,payload_upload,shell_get
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',LoginView.as_view(),name="login"),
    path('index',Index,name='index'),
    path('D_shellcode',file_trojan,name='D_shellcode'),
    path('Data_clear',Data_clear,name='Data_clear'),
    path('upload_file',upload_file,name='upload_file'),
    path('payload',payload,name='payload'),
    path('logout',logout,name='logout'),
    path('history',history,name='history'),
    path('p_remove',payload_del,name='p_remove'),
    path('p_download',payload_download,name='p_download'),
    path('console_get',console_get,name='console_get'),
    path('Actinfo__clear',Actinfo__clear,name='Actinfo__clear'),
    path('',LoginView.as_view()),
    path('exploit',exploit,name='exploit'),
    path('session',session,name='session'),
    path('exploit_button',exploit_button,name='exploit_button'),
    path('exploit_save',exploit_save,name='exploit_save'),
    path('payload_upload',payload_upload,name='payload_upload'),
    path('shell_get',shell_get,name='shell_get'),


]

