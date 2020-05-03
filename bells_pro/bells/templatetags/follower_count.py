from django import template
from ..models import User

register = template.Library() # Djangoのテンプレートタグライブラリ

@register.simple_tag
def follower_count(user_id, trainer_id):
    trainer = User.objects.all().filter(id=trainer_id)
    followers_count = trainer[0].followers.count()

    return followers_count
