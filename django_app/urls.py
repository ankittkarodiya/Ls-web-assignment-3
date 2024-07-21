from django.urls import path
from . import views
from .views import home_view, register_view, login_view, logout_view, profile


app_name = 'django_app'  # Define the namespace here

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),  # Ensure you have a home_view function in views.py
    path('profile/', views.profile, name='profile'),
]
