from django.http import HttpResponse
from django.shortcuts import render
from ..models import User

def index(request):
    return render(request, 'bells/index.html')
 

def likes(request, user_id, article_id):
    """いいねボタンをクリック"""
    if request.method == 'POST':
        user = User.objects.get(id = user_id)
        article = Article.objects.get(id = article_id)
        like_check = User.objects.filter(likes=article).filter(id=user_id)
        if like_check.count() == 0:
            user.likes.add(article)
            user.save()
        else:
            user.likes.remove(article)
            user.save()
        
        context = {
            'like_number': like_check.count()
        }

        # necessary return?
        return HttpResponse("ajax is done!")

def follow(request, user_id, trainer_id):
    # followボタンをクリック
    if request.method == 'POST':
        user = User.objects.get(id = user_id)
        trainer = User.objects.get(id=trainer_id)
        # トレーナーのフォロワーの中に自分がいるかをチェック
        follow_check = trainer.followers.filter(id=user_id)

        if follow_check.count() == 0:
            user.follows.add(trainer)
            user.save()
        else:
            user.follows.remove(trainer)
            user.save()
        
        context = {
            'follow_number' : follow_check.count()
        }

        return HttpResponse("ajax is done!")    
