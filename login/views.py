from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def login(request):
    return render('login.html')

def success(request):
    return redirect('/success')

def createUser(request):
    errors = User.objects.registerValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    else:
        hashpassword = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    return redirect('/success')