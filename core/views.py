from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'core/home.html', 
    )