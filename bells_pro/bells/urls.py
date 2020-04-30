from django.urls import path
from . import views

app_name = 'bells'


urlpatterns = [
    path('', views.defs.index, name='index'),
    path('login/', views.user_login.UserLoginView.as_view(), name='login'),
    path('dashboard/<str:user>', views.dashboard.DashBoardView.as_view(), name='dashboard'),
    path('article_create/<str:user>', views.article_create.ArticleCreateView.as_view(), name='article_create'),
    path('articles/<str:user>', views.article_list.ArticleListView.as_view(), name='articles'),
    path('article/<str:username>/<int:pk>', views.article.ArticleView.as_view(), name='article'),
    path('signup/', views.signup.SignUpView.as_view(), name='signup'),
    path('likes/<int:user_id>/<int:article_id>', views.defs.likes, name='likes'),
]