from django.contrib import admin
from .models import Article, Tags, Category, Carousel
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'created_time']
    ordering = ['-id',]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'father', 'rank', 'urlname']

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'context', 'showFlag']
    ordering = ['-id']
    list_editable = ['showFlag']