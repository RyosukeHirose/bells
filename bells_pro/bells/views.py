from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.views import generic
from .form import UserCreateForm, UserLoginForm, ArticleForm, MyForm
from django.contrib.auth import (
     get_user_model, logout as auth_logout,
)
from django.contrib.auth.views import LoginView
from .models import Article

from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

def index(request):
    return render(request, 'bells/index.html')
 

def likes(request, user_id, article_id):
    """いいねボタンをクリック"""
    if request.method == 'POST':
        user = User.objects.get(id = user_id)
        print(user.username)
        article = Article.objects.get(id = article_id)
        like_check = User.objects.filter(likes=article).filter(id=user_id)
        if like_check.count() == 0:
            user.likes.add(article)
            user.save()
            print('--------いいねつける----------')

        else:
            print('--------いいねつけない----------')
            print(like_check.count())
            user.likes.remove(article)
            user.save()
        
        context = {
            'like_number': like_check.count()
        }

        # necessary return?
        return HttpResponse("ajax is done!")


class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ArticleCreateView(generic.CreateView, LoginRequiredMixin):
    # markdown
    form_class = ArticleForm
    # MediumEditorの場合
    # form_class = MyForm
    template_name = 'dashboard/article_create.html'

    def get_success_url(self):
        print("---------")
        print(self.request.user.username)
        return reverse('bells:article', kwargs={'user': self.request.user.username})




class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'

    swappable = 'AUTH_USER_MODEL'

class DashBoardView(generic.TemplateView, LoginRequiredMixin):
    template_name='dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        articles = Article.objects.all().order_by('id')[0:3]
        context = super().get_context_data(**kwargs)
        context['articles'] = articles
        context['user'] = self.request.user
        context['username'] = self.request.user.username
        context['likes_count'] =  self.request.user.likes.count()
        return context



class ArticlesView(generic.TemplateView, LoginRequiredMixin):
    articles = Article.objects.all()
    template_name='dashboard/articles.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context

class ArticleView(generic.DetailView, LoginRequiredMixin):
    model = Article
    template_name = 'dashboard/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        login_user = self.request.user
        print(login_user.id)
        context['articles'] = Article.objects.get(id=self.kwargs['pk'])
        context['likes_number'] =  context['articles'].user_likes.count()

        like_check = User.objects.filter(likes=context['articles']).filter(id=login_user.id).count()
        context['like_check'] = False if like_check == 0 else True
        context['login_user'] = login_user


        return context
