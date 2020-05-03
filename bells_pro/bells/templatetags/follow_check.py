from django import template
from ..models import User
from django.template.defaultfilters import register

@register.filter("follow_check")
def follow_check(trainer, user_id):
    trainer = User.objects.all().filter(id=trainer.id)
    followers_check = trainer[0].followers.filter(id=user_id).count()
    follow_check = True if followers_check > 0 else False

    return followers_check