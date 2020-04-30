from django.db import models
from mdeditor.fields import MDTextField
# from mediumeditor.widgets import MediumEditorTextarea
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .user import User


class Article(models.Model):
    title = models.CharField(max_length=70)
    detail = MDTextField()
    # detail = models.TextField()
    # detail = MediumEditorTextarea()
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    updated_at = models.DateTimeField('更新日', default=timezone.now)

    user_likes = models.ManyToManyField(
        User,
        related_name="likes",
        blank=True,
    )

    user_favorites = models.ManyToManyField(
        User,
        related_name="favorites",
        blank=True,
    )
    def __str__(self):
        return self.title
