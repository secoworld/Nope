from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'article'

urlpatterns =[
    path('article/<int:aid>', views.article_show, name="detail"),
    path('category/<urlname>', views.category_list, name="category"),
    path('tags/<tag>', views.tag_list, name="tags"),
    path('search/', views.Search, name="search"),
    path('', views.index, name="home"),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)