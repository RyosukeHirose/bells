from django.db import models
from django.utils.translation import gettext_lazy as _
from .user import User
from .article import Article



class Comment(models.Model):
    comment = models.CharField(max_length=256)
    article = models.ForeignKey(
        Article, 
        related_name="comments",
        on_delete=models.CASCADE,
        )
    user = models.ForeignKey(
        User, 
        related_name="commets",
        on_delete=models.SET_NULL, 
        null = True
        )

class Tag(models.Model):
    tag = models.CharField(max_length=20)
    article = models.ManyToManyField(
        Article,
        related_name="tags",
        blank=True,
    )

class QuestionBox(models.Model):
    detail = models.TextField()
    user = models.ForeignKey(
        User,
        related_name="question_box",
        on_delete=models.CASCADE
    )

class Answer(models.Model):
    question_box = models.ForeignKey(
        QuestionBox,
        related_name = "answers",
        on_delete=models.CASCADE
    )
    User = models.ForeignKey(
        User,
        related_name="answers",
        on_delete=models.SET_NULL,
        null=True
    )
