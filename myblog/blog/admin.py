from django.contrib import admin
from .models import Tags, Category, Article

# Register your models here.
@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url_name','index']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_time']
    list_editable = ['title', 'author']
    ordering = ['-created_time',]