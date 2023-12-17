from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from accounts.forms import UserRegisterForm


# Create your views here.
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)

        return redirect('EquipoList')

    form = AuthenticationForm()
    contexto = {
        'form': form
    }
    return render(request, 'accounts/login.html', contexto)


def register_request(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('EquipoList')

    form = UserRegisterForm()
    contexto = {
        'form': form
    }
    return render(request, 'accounts/registro.html', contexto)


@login_required
def editar_request(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('EquipoList')

    user = request.user
    form = UserRegisterForm(initial={'username': user.username, 'email': user.email})
    contexto = {
        'form': form
    }
    return render(request, 'accounts/registro.html', contexto)

