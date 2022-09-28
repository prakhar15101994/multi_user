
from django.contrib import admin
from django.urls import path,include
from accounts import views

urlpatterns = [
    
    path('login/', views.login_page, name='login'),
    path('', views.register_page, name='register'),
    path('profile/', views.profile_page, name='profile'),
    path('logout/', views.logout_user, name='logout'),
]
