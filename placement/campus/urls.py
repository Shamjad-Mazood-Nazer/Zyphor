from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import applyDrive

app_name = 'campus'

urlpatterns = [
    path('', views.home, name='home'),

    path('tpo', views.tpo, name='tpo'),
    path('tpoLogin', views.tpoLogin, name='tpoLogin'),
    path('adminDash', views.adminDash, name='adminDash'),
    path('tpoLogout', views.tpoLogout, name='tpoLogout'),

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('studentDash', views.studentDash, name='student'),
    path('updateStudentDetails', views.updateStudentDetails, name='updateStudentDetails'),
    path('logout', views.logout, name='logout'),

    path('viewDrive', views.viewDrive, name='viewDrive'),
    path('registerDrive', views.registerDrive, name='registerDrive'),
    path('applyDrive', views.applyDrive, name='applyDrive'),
    # path('applyDrive/<drive_id>/', applyDrive.as_view(), name='applyDrive'),

    path('payment', views.payment, name='payment'),
    path('thanks', views.thanks, name='thanks'),

    path('quiz', views.quiz, name='quiz'),
    path('quiz_mode', views.quiz_mode, name='quiz_mode'),
    path('quiz_list', views.quiz_list, name='quiz_list'),
    path('quiz_detail', views.quiz_detail, name='quiz_detail'),

    path('ajax_generate_code/', views.ajax_generate_code, name='ajax_generate_code'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='campus/password_reset.html'),
         name='reset_password'),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='campus/password_reset_sent.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/token/',
         auth_views.PasswordResetConfirmView.as_view(template_name='campus/password_reset_form.html'),
         name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='campus/password_reset_done.html'),
         name='password_reset_complete'),
]
