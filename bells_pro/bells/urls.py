from django.urls import path
from . import views

app_name = 'bells'


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('dashboard/<str:user>', views.DashBoardView.as_view(), name='dashboard'),
    path('article_create/<str:user>', views.ArticleCreateView.as_view(), name='article_create'),
    path('articles/<str:user>', views.ArticlesView.as_view(), name='articles'),
    path('article/<str:username>/<int:pk>', views.ArticleView.as_view(), name='article'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('likes/<int:user_id>/<int:article_id>', views.likes, name='likes'),
]