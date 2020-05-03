from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models.article import Article

User = get_user_model()

class ArticleView(generic.DetailView, LoginRequiredMixin):
    model = Article
    template_name = 'dashboard/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        login_user = self.request.user
        context['articles'] = Article.objects.get(id=self.kwargs['pk'])
        context['likes_number'] =  context['articles'].user_likes.count()

        like_check = User.objects.filter(likes=context['articles']).filter(id=login_user.id).count()
        context['like_check'] = False if like_check == 0 else True
        context['login_user'] = login_user


        return context