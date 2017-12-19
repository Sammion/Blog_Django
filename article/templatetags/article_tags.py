from django import template

# django 模板类库中有很多类和方法
# 这里用一个Libray类，创建一个实例
register = template.Library()

from article.models import ArticlePost
from django.db.models import Count

@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()


@register.simple_tag
def author_total_articles(user):
    return user.article.count()


# 返回字典数据到指定的HTML页面
@register.inclusion_tag('article/list/lastest_articles.html')
def lastest_articles(n=5):
    lastest_articles = ArticlePost.objects.order_by('-created')[:n]
    return {"lastest_articles": lastest_articles}


@register.assignment_tag
def most_commented_articles(n=3):
    #annotate函数对各个文章对象标注，用comments的总数来标注
    return ArticlePost.objects.annotate(total_comments=Count('comments')).order_by("-total_comments")[:n]