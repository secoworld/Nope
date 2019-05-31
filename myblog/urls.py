"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
#导入静态文件
from django.views.static import serve
#导入配置文件上的配置
from django.conf import  settings
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ueditor', include('DjangoUeditor.urls')),
    #增加对图片上传路径
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    #path('blog/', include('blog.urls')),
    path('', views.index, name="index"),
    path('tags/<tag>', views.tags, name="tags"),
    path('s/', views.search, name="search"),
    path('show-<int:sid>', views.show, name="show"),
    path('list-<int:lid>', views.list ,name="list")
]
