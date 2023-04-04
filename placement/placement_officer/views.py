from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *


# create your views here.

def admin_login(request):
    if request.method == 'POST':
        admin_email = 'tpo@ajce.in'
        admin_password = 'Admin@123'
        email = request.POST['email']
        password = request.POST['password']
        if admin_email == email and admin_password == password:
            return redirect('placement_officer:admin_dashboard')
    return render(request, 'placement_officer/login.html')


def admin_dashboard(request):
    return render(request, 'placement_officer/dashboard_base.html')
