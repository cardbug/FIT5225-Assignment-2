from django import forms
from  django.contrib.auth.models import User as UserInfo
class LoginForm(forms.Form):
    username=forms.CharField(
        required=True,
        error_messages={"required": "姓名不能为空"},
        widget=forms.TextInput(attrs={"class": "layui-input","placeholder":"请输入姓名"})
    )
    password=forms.CharField(
        required=True,
        error_messages={"required": "密码不能为空"},
        widget=forms.PasswordInput(attrs={"class": "layui-input","placeholder":"请输入密码"})
    )
    def clean_username(self):
        username=self.cleaned_data["username"]
        if  not UserInfo.objects.filter(username=username).exists():
            return  self.add_error("username","用户名不存在")
        return self.cleaned_data["username"]