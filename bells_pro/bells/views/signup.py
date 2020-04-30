from django.views import generic
from django.urls import reverse_lazy
from ..form import UserCreateForm



class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'