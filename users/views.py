from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from rolepermissions.roles import assign_role


def sign_in(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'sign-in.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

    if not password == password_confirm:
        messages.add_message(
            request, constants.ERROR,
            'A senha e a confirmação devem estar iguais.'
        )
        return redirect('sign-in')

    MIN_PASSWORD_LEN = 6
    if len(password) < MIN_PASSWORD_LEN:
        messages.add_message(
            request, constants.ERROR,
            'A senha precisa ter ao menos 6 caracteres.'
        )

    user = User.objects.filter(username=username)
    if user.exists():
        messages.add_message(
            request, constants.ERROR,
            'Esse usuário já está cadastrado.'
        )
        return redirect('sign-in')

    User.objects.create_user(username=username, password=password)
    return redirect('login')


def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('ai_trainning')

        messages.add_message(
            request, constants.ERROR,
            'Usuário ou senha inválidos.'
        )
        return redirect('login')


@user_passes_test(lambda u: u.is_superuser)
def permissions(request: HttpRequest) -> HttpResponse:
    users = User.objects.filter(is_superuser=False)
    return render(request, 'permissions.html', {'users': users})


def manager_permission(request: HttpRequest, id: int) -> HttpResponse:
    user = User.objects.get(id=id)
    assign_role(user, 'manager')
    return redirect('permissions')
