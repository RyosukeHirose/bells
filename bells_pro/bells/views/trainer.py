from django.views import generic
from django.urls import reverse

from ..models.user import User

class TrainerView(generic.DetailView):
    model = User
    template_name = "dashboard/trainer_detail.html"
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        print(self.kwargs['slug'])

        context = super().get_context_data(**kwargs)
        context['trainer'] = User.objects.get(username=self.kwargs['slug'])
        # context['follower'] = context['trainer'][0].followers.count()
        # context['articles'] = context['follower'].trainer_set

        return context
