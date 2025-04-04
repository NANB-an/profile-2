from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User

def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('profile')
            else:
                messages.error(request, "Invalid credentials")
    else:
        form = LoginForm()

    return render(request, 'myprofileApp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login')
def register_view(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']

            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password,
                                            first_name=first_name, last_name=last_name)
            user.save()

            # Log the user in automatically after registration
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()

    return render(request, 'myprofileApp/register.html', {'form': form})


