from django.shortcuts import render,redirect, reverse
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm

# Create your views here.
def loginView(request):
    forms = LoginForm()
    if request.user.is_authenticated:
        return redirect(reverse('article:home'))

    if request.method == 'POST':
        formtext = LoginForm(request.POST)

        if formtext.is_valid():
            username = formtext.cleaned_data['username']
            password = formtext.cleaned_data['password']
            next_page = formtext.cleaned_data['next_page']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                if next_page is not None and next_page != 'None':
                    return redirect(next_page)
                else:
                    return redirect(reverse('article:home'))

        else:
            message = "用户名或者密码错误"
            return render(request, 'login.html', locals())


    elif request.method == 'GET':
        next_page = request.GET.get('next_page')

    return render(request, 'login.html', locals())


def logoutView(request):
    logout(request)
    return redirect(reverse('article:home'))


def registerView(request):
    forms = RegisterForm()
    if request.user.is_authenticated:
        return redirect(reverse('article:home'))

    if request.method == 'POST':
        formtext = RegisterForm(request.POST)
        if formtext.is_valid():
            username = formtext.cleaned_data['username']
            password1 = formtext.cleaned_data['password1']
            password2 = formtext.cleaned_data['password2']
            email = formtext.cleaned_data['email']
            next_page = formtext.changed_data['next_page']

            if password1 != password2:
                message = "两次输入的密码不同"
                return render(request, 'register.html', locals())

            same_username = User.objects.filter(username=username)
            if same_username:
                message="用户名已经存在"
                return render(request, 'register.html', locals())
            
            if User.objects.filter(email=email):
                message = "邮箱已经存在"
                return render(request, 'register.html', locals())

            user = User.objects.create_user(username, email)
            user.set_password(password1)
            user.save()

            return render(request, 'login.html', locals())
        
    elif request.method == 'GET':
        next_page = request.GET.get('next_page')

    return render(request, 'register.html', locals())
