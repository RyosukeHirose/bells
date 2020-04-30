from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'bells/index.html')
 

def likes(request, user_id, article_id):
    """いいねボタンをクリック"""
    if request.method == 'POST':
        user = User.objects.get(id = user_id)
        print(user.username)
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