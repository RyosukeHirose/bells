from django.contrib import admin

from .models.article import Article
from .models.article import User

admin.site.register(Article)
admin.site.register(User)

