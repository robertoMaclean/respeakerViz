# accounts/urls.py
from django.urls import path
from apps.accounts import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('register/', views.register_view, name = 'register'),
    path('password/', views.change_password, name='change_password'),
]