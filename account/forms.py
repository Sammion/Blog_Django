from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


# 登陆表单
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# 注册表单
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='请输入密码：', widget=forms.PasswordInput)
    password2 = forms.CharField(label='请再次输入密码：', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('密码两次输入不匹配')
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("cellphone", "birth", "hobby")
