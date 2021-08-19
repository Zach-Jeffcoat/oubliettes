from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'index.html')

def success(request):
    if "userid" in request.session:
        return render(request, 'success.html')
    else:
        return redirect('/')
    
def login(request):
    user = User.objects.filter(username=request.POST['username'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/success')
    return redirect("/")


def logout(request):
    pass

def register(request):
    errors = User.objects.registerValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    else:
        hashpassword = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        request.session['userid']=request.POST['userid']
    return redirect('/success')