from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views import generic
from .form import UserCreateForm, UserLoginForm
from django.contrib.auth import (
     get_user_model, logout as auth_logout,
)
from django.contrib.auth.views import LoginView

User = get_user_model()

def index(request):
    return render(request, 'bells/index.html')
 
 
@login_required
def home(request):
    return render(request, 'bells/home.html')

class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserLoginVuew(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'


