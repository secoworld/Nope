from django.urls import path
from . import views

app_name = 'users'

urlpatterns =[
    path('login/', views.loginView, name="login" ),
    path('logout/', views.logoutView, name="logout" ),
    path('register/', views.registerView, name="register" ),
]