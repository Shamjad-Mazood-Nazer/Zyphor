from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *


# create your views here.

def admin_login(request):
    return render(request, 'placement_officer/login.html')
