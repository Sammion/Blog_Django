from django.contrib import admin
from .models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'cellphone')
    list_filter = ('cellphone', 'birth')


admin.site.register(UserProfile, UserProfileAdmin)
