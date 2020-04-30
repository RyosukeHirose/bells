# from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse
# from django.shortcuts import redirect
# from django.shortcuts import render
# from django.urls import reverse

# from django.views import generic
# from .form import UserCreateForm, UserLoginForm, ArticleForm, MyForm
# from django.contrib.auth import (
#      get_user_model, logout as auth_logout,
# )
# from django.contrib.auth.views import LoginView
# from .models.article import Article

# from django.contrib.auth.mixins import LoginRequiredMixin
# import datetime


# User = get_user_model()

# def index(request):
#     return render(request, 'bells/index.html')
 

# def likes(request, user_id, article_id):
#     """いいねボタンをクリック"""
#     if request.method == 'POST':
#         user = User.objects.get(id = user_id)
#         print(user.username)
#         article = Article.objects.get(id = article_id)
#         like_check = User.objects.filter(likes=article).filter(id=user_id)
#         if like_check.count() == 0:
#             user.likes.add(article)
#             user.save()
#         else:
#             user.likes.remove(article)
#             user.save()
        
#         context = {
#             'like_number': like_check.count()
#         }

#         # necessary return?
#         return HttpResponse("ajax is done!")


# class SignUpView(generic.CreateView):
#     form_class = UserCreateForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


# class ArticleCreateView(generic.CreateView, LoginRequiredMixin):
#     # markdown
#     form_class = ArticleForm
#     # MediumEditorの場合
#     # form_class = MyForm
#     template_name = 'dashboard/article_create.html'

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.trainer = self.request.user
#             obj.save()
            
#             return redirect('bells:articles', user=self.request.user)


# class UserLoginView(LoginView):
#     form_class = UserLoginForm
#     template_name = 'registration/login.html'

#     swappable = 'AUTH_USER_MODEL'

# class DashBoardView(generic.TemplateView, LoginRequiredMixin):
#     template_name='dashboard/dashboard.html'

#     def get_context_data(self, **kwargs):
#         today = datetime.datetime.now()
#         last_week = today - datetime.timedelta(weeks=2)
        
#         articles = Article.objects.all().order_by('created_at').reverse()[0:3]
#         pickups = Article.objects.filter(created_at__gt=last_week, created_at__lt=today).order_by('user_likes').reverse()[0:3]
#         context = super().get_context_data(**kwargs)
#         context['articles'] = articles
#         context['pickups'] = pickups

#         context['user'] = self.request.user
#         context['username'] = self.request.user.username
#         context['likes_count'] =  self.request.user.likes.count()

#         return context



# class ArticlesView(generic.TemplateView, LoginRequiredMixin):
#     articles = Article.objects.all()
#     template_name='dashboard/articles.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['articles'] = Article.objects.all().order_by('created_at').reverse()
#         return context

# class ArticleView(generic.DetailView, LoginRequiredMixin):
#     model = Article
#     template_name = 'dashboard/article_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         login_user = self.request.user
#         print(login_user.id)
#         context['articles'] = Article.objects.get(id=self.kwargs['pk'])
#         context['likes_number'] =  context['articles'].user_likes.count()

#         like_check = User.objects.filter(likes=context['articles']).filter(id=login_user.id).count()
#         context['like_check'] = False if like_check == 0 else True
#         context['login_user'] = login_user


#         return context
