from django.contrib import admin

# Register your models here.
from Demo.models import Login,console_status,online,Exploitinfo_save

admin.site.register(Login)
admin.site.register(online)
admin.site.register(console_status)
admin.site.register(Exploitinfo_save)