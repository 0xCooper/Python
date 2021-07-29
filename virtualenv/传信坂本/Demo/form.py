from django import forms
class LoginForm(forms.Form):
    ip =forms.CharField(max_length=15)
    port = forms.CharField(max_length=5)
    user=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)

class shellcode(forms.Form):
    lhost =forms.CharField(max_length=15)
    lport = forms.CharField(max_length=5)
    name = forms.CharField(max_length=20)
    env=forms.CharField(max_length=8)