from django.contrib import admin
from .models import UserProfile, UserInfo


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'cellphone')
    list_filter = ('cellphone', 'birth')


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'school', 'company', 'profession', 'address', 'aboutme')
    list_filter = ('school', 'company', 'profession')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
