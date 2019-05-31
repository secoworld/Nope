#myblog 的url设置
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
]