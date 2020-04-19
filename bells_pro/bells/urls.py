from django.urls import path
from . import views

app_name = 'bells'


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.UserLoginVuew.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('home/', views.home, name='home'),
]