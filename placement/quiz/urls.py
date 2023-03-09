from django.urls import path
from .views import *


app_name = 'quiz'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', QuizCreateView.as_view(), name='create'),
    path('<int:quiz_id>/', QuizDetailView.as_view(), name='detail'),
]
