from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm
# Create your views here.
class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

class UserLogoutView(LogoutView):
    next_page = "login"