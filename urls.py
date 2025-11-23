"""
URL configuration for myproject project.
"""
from django.contrib import admin
from django.urls import path
from auth_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name='login'),
    path('main/', views.main_page, name='main'),
]

