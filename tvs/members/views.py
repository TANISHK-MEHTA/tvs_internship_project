from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User

def register_user(request):
    if request.method == 'POST':
        
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.success(request, ("That username is taken"))
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            # Login after register
            # auth.login(request, user)
            # messages.success(request, ("You are now logged in"))
            # return redirect('index')
            user.save()
            messages.success(request, ("You are now registered and can log in"))
            return redirect('login')
       
    else:
        return render(request, 'members/register.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in!"))
            return redirect('home')
        else:
            messages.success(request, ("Error logging in - please try again..."))
            return redirect('login')
    return render(request, 'members/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out..."))
    return redirect('login')