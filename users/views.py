from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import logout as logout_user

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                form.save()
                messages.success(request, f'Your account has been created! You are now able to log in')
                return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    return render(request, 'users/profile.html')

@login_required
def logout(request):
    logout_user(request)
    messages.info(request, "You are now logged out.")
    return redirect('login')