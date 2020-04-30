from django.contrib.auth.views import LoginView
from ..form import UserLoginForm

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'

    swappable = 'AUTH_USER_MODEL'