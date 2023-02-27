from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog-home')

        else:
            messages.success(request,("Sorry, username or password was incorrect. Try Again.."))
            return redirect('login')
    
    return render(request, 'users/login.html',{})

def logout_user(request):
    logout(request)
    return render(request, 'users/login.html')
    

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created {username} ! You are now able to login')
            return redirect('login')
        else:
            messages.success(request,("Sorry, Passwords do NOT match Try Again..."))
            return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')