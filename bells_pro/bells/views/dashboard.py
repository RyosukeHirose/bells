from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models.article import Article
import datetime

class DashBoardView(generic.TemplateView, LoginRequiredMixin):
    template_name='dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        today = datetime.datetime.now()
        last_week = today - datetime.timedelta(weeks=2)
        
        articles = Article.objects.all().order_by('created_at').reverse()[0:3]
        pickups = Article.objects.filter(created_at__gt=last_week, created_at__lt=today).order_by('user_likes').reverse()[0:3]
        context = super().get_context_data(**kwargs)
        context['articles'] = articles
        context['pickups'] = pickups

        context['user'] = self.request.user
        context['username'] = self.request.user.username
        context['likes_count'] =  self.request.user.likes.count()

        return context