from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        # print('=====================》《=======================')
        # print(request.path)
        # print(request.GET)
        # print(request.POST)
        # print(request.COOKIES)
        # print(request.META)
        # print(request.is_ajax())
        # print(request.is_secure())
        # print('=====================》《=======================')
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("欢迎登陆我的博客!")
            else:
                return HttpResponse("对不起，你输入的密码有误！")
        else:
            return HttpResponse("未认证的用户！")
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, "account/login.html", {'form': login_form})


# 用户注册
def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse('Successfully register.')
        else:
            return HttpResponse('Sorry, you can not register.')
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, 'account/register.html', {'form': user_form, 'profile': userprofile_form})
