from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm
from .forms import UserRegisterForm
from django.contrib.auth.models import User
# 引入验证登录的装饰器
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法的数据
            data = user_login_form.cleaned_data
            # 检测账号密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个user对象
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 将用户的数据保存在session中，实现了登录的动作
                login(request, user)
                return redirect("blog:home")
            else: 
                return HttpResponse("账号或密码输入错误，请重新输入")
        else:
            return HttpResponse("账号或密码不合法")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, 'login.html', context)

    else:
        return HttpResponse("请使用GET或者POST请求数据")


# 退出登录
def user_logout(request):
    logout(request)
    return redirect("blog:home")

# 用户注册
def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # 设置密码
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # 保存好数据以后，立即登录并韩慧博客的列表页面、
            login(request, new_user)
            return redirect("blog:home")
        else:
            return HttpResponse("注册表单有误，请重新输入~")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = {'form': user_register_form }
        return render(request, 'register.html', context)
    else: 
        return HttpResponse("请使用GET或者POST请求数据")


@login_required(login_url='login')
def user_delete(request, id):
    user = User.objects.get(id=id)
    # 验证登录的用户和待删除的用户是否相同
    if request.user == user:
        # 退出登录，删除数据并返回到博客列表
        logout(request)
        user.delete()
        return redirect("blog:home")
    else: 
        return HttpResponse("你没有删除操作的权限")
