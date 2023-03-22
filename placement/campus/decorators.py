from .models import StudentReg
from django.shortcuts import redirect


def user_login_required(function):
    def wrapper(request, *args, **kwargs):
        if not 'email' in request.session:
            return redirect('/')
        else:
            return function(request, *args, **kwargs)

    return wrapper
