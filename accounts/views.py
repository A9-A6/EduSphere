
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import Profile
from universities.models import University


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect('home')

        messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        university_code = request.POST.get('university', '')

        if not username or not email or not password1:
            messages.error(request, 'Please complete all required fields.')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'This username is already taken.')

        elif User.objects.filter(email__iexact=email).exists():
            messages.error(request, 'This email is already registered.')

        elif password1 != password2:
            messages.error(request, 'Passwords do not match.')

        else:
            try:
                validate_password(password1)

                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1
                )

                university = University.objects.filter(
                    short_name__iexact=university_code
                ).first()

                Profile.objects.create(
                    user=user,
                    university=university
                )

                messages.success(
                    request,
                    'Your account has been created successfully.'
                )
                return redirect('login')

            except ValidationError as error:
                for message in error.messages:
                    messages.error(request, message)

    return render(request, 'accounts/register.html')
