from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.text import slugify
from urllib.parse import quote
import uuid


# pip install redis

# Create your models here.

class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='article_column')
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column


class ArticlePost(models.Model):
    author = models.ForeignKey(User, related_name="article")
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    column = models.ForeignKey(ArticleColumn, related_name='article_column')
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)
    users_like = models.ManyToManyField(User, related_name="articles_like", blank=True)

    class Meta:
        ordering = ("title",)
        # 创建索引
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    # 重写保存方法
    def save(self, *args, **kargs):
        # print('==========================>',self.title.decode('utf8'))

        # self.slug = quote(self.title)
        self.slug = uuid.uuid1()
        super(ArticlePost, self).save(*args, **kargs)

    # 获取某个文章的url
    def get_absolute_url(self):
        return reverse("article:article_detail", args=[self.id, self.slug])


class Comment(models.Model):
    article = models.ForeignKey(ArticlePost, related_name="comments")
    commentator = models.CharField(max_length=90)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "commented by {0} on {1}.".format(self.commentator.username, self.article)

