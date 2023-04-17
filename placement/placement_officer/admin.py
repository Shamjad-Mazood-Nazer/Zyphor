from django.contrib import admin
from .models import *


class TPO(Admin):
    list_display = ['first_name',]


admin.site.register(Admin)
