from django import forms
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.models import User, Group
from django.core import validators
from django.core.exceptions import ValidationError
from django.http import HttpResponse

from django.shortcuts import render, redirect

from user.models import userProfile
from utils.FormManager import BootstrapForm, gen_random_str


# gen_random_str

# Create your views here.


class RegisterForm(BootstrapForm):
    username = forms.CharField(
        label='账号',
        widget=forms.TextInput,
        required=True,
        validators=[validators.MinLengthValidator(7), validators.MaxLengthValidator(10), validators.integer_validator],
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput,
        required=True,
        validators=[validators.MinLengthValidator(6)]

    )
    confirm = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput,
        required=True,
    )

    def clean_username(self):

        username = self.cleaned_data.get('username')

        exist = userProfile.objects.filter(user__username=username)

        if exist:
            raise ValidationError('用户已存在')

        return username

    def clean_confirm(self):
        pwd = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if all([pwd, confirm]) and confirm != pwd:
            raise ValidationError('密码不一致')

        return confirm


def register(request):
    # print(111)
    if request.method == 'GET':

        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == 'POST':

        form = RegisterForm(data=request.POST)

        if form.is_valid():
            # print(form.cleaned_data)
            group = Group.objects.get(name='普通用户')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # nickname =
            user = User.objects.create_user(
                username=username,
                password=password
            )
            user.groups.add(group)

            nickname = "user" + gen_random_str(5)

            userProfile.objects.create(nickname=nickname, user=user)
            return redirect('/login/')
        else:
            return render(request, './register.html', {'form': form})


class LoginForm(BootstrapForm):
    username = forms.IntegerField(
        label='账号',
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput,
        required=True,

    )

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        exists = authenticate(username=username, password=password)

        if not exists:
            raise ValidationError('账号不存在或密码错误')

        return password


def Login(request):
    if request.method == 'GET':

        if (request.user.id != None):
            return redirect('/')

        form = LoginForm()
        return render(request, './login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            print(user)

            if user and user.is_active:
                login(request, user)
                print(user)
                return redirect('/')
            else:

                return render(request, './login.html', {'form': form})

        else:
            # form = LoginForm(data=request.POST)
            return render(request, './login.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('/')

