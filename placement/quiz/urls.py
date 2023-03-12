from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('quiz_mode', views.quiz_mode, name='quiz_mode'),
    path('upload/', views.upload_aiken, name='upload_aiken'),
]
