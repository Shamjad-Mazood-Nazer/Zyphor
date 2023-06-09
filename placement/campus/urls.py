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

    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('update_password', views.update_password, name='update_password'),
    path('password_changed', views.password_changed, name='password_changed'),
    path('studentDash', views.studentDash, name='student'),
    path('student_profile', views.student_profile, name='student_profile'),
    path('updateStudentDetails', views.updateStudentDetails, name='updateStudentDetails'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('change_profile_picture', views.change_profile_picture, name='change_profile_picture'),
    path('logout', views.logout, name='logout'),

    path('viewDrive', views.viewDrive, name='viewDrive'),
    path('register_drive/<int:id>/', views.register_drive, name='register_drive'),

    path('payment', views.payment, name='payment'),
    path('thanks', views.thanks, name='thanks'),
    path('pay_error', views.pay_error, name='pay_error'),
    path('receipt/', views.generate_receipt, name='generate_receipt'),

    path('quiz', views.quiz, name='quiz'),
    path('quiz_mode', views.quiz_mode, name='quiz_mode'),
    path('quiz_list', views.quiz_list, name='quiz_list'),
    path('quiz_detail/<int:id>/', views.quiz_detail, name='quiz_detail'),

    path('submit_quiz/<int:id>/', views.submit_quiz, name='submit_quiz'),

    path('ajax_generate_code/', views.ajax_generate_code, name='ajax_generate_code'),

    path('sent_message', views.sent_message, name='sent_message'),

    path('teacher_login', views.teacher_login_view, name='teacher_login'),
    path('teacher_logout', views.teacher_logout_view, name='teacher_logout'),
    path('teacher_dashboard', views.teacher_dashboard, name='teacher'),
    path('teacher_profile', views.teacher_profile, name='teacher_profile'),
    path('teacher_update_password', views.teacher_update_password, name='teacher_update_password'),
    path('student_list', views.student_list, name='student_list'),
    path('update_cgpa/<int:id>/', views.teacher_update_mca, name='update_cgpa'),

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
