from django.contrib import admin
from .models import FriendLink
# Register your models here.
@admin.register(FriendLink)
class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'create_time']
    ordering = ['-create_time']