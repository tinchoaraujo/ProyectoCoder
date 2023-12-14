from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import login_request, register_request

urlpatterns = [
    path('register/', register_request, name='Registro'),
    path('login/', login_request, name='Login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='Logout'),
    ]
