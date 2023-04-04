from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'placement_officer'

urlpatterns = [
    path('admin_login', views.admin_login, name='admin_login')
]
