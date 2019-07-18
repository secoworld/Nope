from django.urls import path, include
from . import views

app_name = 'article'

urlpatterns =[
    path('article/<int:id>', views.article_show, name="detail"),
    path('category/<urlname>', views.category_list, name="category"),
    path('tags/<tag>', views.tag_list, name="tags"),
    path('', views.index, name="home"),
]