from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models.article import Article


class ArticleListView(generic.TemplateView, LoginRequiredMixin):
    articles = Article.objects.all()
    template_name='dashboard/articles.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('created_at').reverse()
        return context