from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    birth = models.DateTimeField(blank=True, null=True)
    cellphone = models.CharField(max_length=20, null=True)
    hobby = models.CharField(max_length=100, null=True)

    def __str__(self):
        return 'user{}'.format(self.user.username)
