from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from ..form import ArticleForm, MyForm


class ArticleCreateView(generic.CreateView, LoginRequiredMixin):
    # markdown
    form_class = ArticleForm
    # MediumEditorの場合
    # form_class = MyForm
    template_name = 'dashboard/article_create.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.trainer = self.request.user
            obj.save()
            
            return redirect('bells:articles', user=self.request.user)
