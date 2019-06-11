from django.contrib import admin
from django.urls import path,include
from . import views

# 设置APP名称
app_name = 'blog'

urlpatterns = [
    # path('', include('blog.urls')),
    path('test/', views.test, name="test" ),
    path('', views.index, name="home"),
    path('article/<int:aid>', views.detail, name="detail"),
    # 分类列表
    path('category/<category_name>', views.category_list, name="category"),
    path('tags/<tag>', views.tag, name="tags"),

]