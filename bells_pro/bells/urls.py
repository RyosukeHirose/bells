from django.urls import path
from . import views

app_name = 'bells'


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    # path('login/<str:type>', views.userlogin, name='login_user'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
]