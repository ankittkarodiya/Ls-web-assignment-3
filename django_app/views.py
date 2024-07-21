from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(f"User registered: {user.username}")  # Debugging line
            return redirect('django_app:home')
        else:
            print("Form errors:", form.errors)  # Debugging line
    else:
        form = RegisterForm()
    return render(request, "django_app/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('django_app:home')  # Use the namespaced URL pattern
    else:
        form = AuthenticationForm()
    return render(request, "django_app/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('django_app:login')  # Ensure 'login' is the correct namespaced URL pattern

def profile(request):
    # return render(request, 'django_app/profile.html')
    return render(request, 'django_app/profile.html', {'user': request.user})


def home_view(request):
    return render(request, "django_app/home.html")
