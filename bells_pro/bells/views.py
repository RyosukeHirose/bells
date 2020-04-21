from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

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

# def userlogin(request, type):
#     email = request.POST['username']
#     return HttpResponseRedirect(reverse('bells:dashboard', args=(type,)))

@login_required
def dashboard(request):
    # type = get_object_or_404(Question, pk=type)
    return render(request, 'bells/dashboard.html')


class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserLoginView(LoginView):
    AUTH_USER_MODEL = 'bells.AdminUser'
    print("------------------------------")
    form_class = UserLoginForm
    template_name = 'registration/login.html'

    swappable = 'AUTH_USER_MODEL'





