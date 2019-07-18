from django.urls import path, include
from . import views

app_name = 'article'

urlpatterns =[
    path('article/<int:id>', views.article_show, name="show"),
    path('category/<urlname>', views.category_list, name="category"),
    path('tags/<tag>', views.tag_list, name="tag"),
    path('', views.index, name="home"),
]