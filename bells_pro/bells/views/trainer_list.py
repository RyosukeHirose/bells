from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models.user import User


class TrainersView(generic.TemplateView, LoginRequiredMixin):
    template_name='dashboard/trainers.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trainers'] = User.objects.all().filter(is_trainer=True)
        context['user'] = self.request.user

        return context
