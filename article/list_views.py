from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import ArticleColumn, ArticlePost
from django.contrib.auth.models import User


def article_titles(request, username=None):
    if username:
        user = User.objects.get(username=username)
        articles_title = ArticlePost.objects.filter(author=user)
        try:
            userinfo = user.userinfo
        except:
            userinfo = None
    else:
        articles_title = ArticlePost.objects.all()

    paginator = Paginator(articles_title, 2)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    if username:
        return render(request, "article/list/article_titles.html",
                      {"articles": articles, "page": current_page, "user": user, "userinfo": userinfo})
    else:
        return render(request, "article/list/article_titles.html",
                      {"articles": articles, "page": current_page})
