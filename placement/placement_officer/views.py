from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *


# create your views here.

def admin_login(request):
    print('test')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        if Admin.objects.filter(email=email, password=password).exists():
            user = Admin.objects.filter(email=email)
            print('outside: ', user)
            for std in user:
                email = std.email
                id = std.id
                print('email', email, 'id: ', id)
                request.session['email'] = std.email
                """This is a session variable and will remain existing as long as you don't delete this manually or 
                clear your browser cache """
                request.session['id'] = id
                return redirect('placement_officer:admin_dashboard')
        error = "Credentials not match! Try again"
        return render(request, 'placement_officer/login.html', {'error': error})
    else:
        return render(request, 'placement_officer/login.html', )


def admin_dashboard(request):
    return render(request, 'placement_officer/dashboard_base.html')


def logout_view(request):
    logout(request)
    return redirect('campus:home')


def error(request):
    return render(request, 'placement_officer/pages-error-404.html')


def profile(request):
    return render(request, 'placement_officer/users-profile.html')
