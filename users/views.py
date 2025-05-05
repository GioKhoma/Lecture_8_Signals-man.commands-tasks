from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from .forms import CustomUserRegisterForm, CustomAuthForm
from django.contrib.auth.decorators import login_required


# login 1
# first starting with simple login without form
# def login_user(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('templates_app:home')
#         else:
#             messages.error(request, "Invalid credentials, please try again.")
#             return redirect('users:login_user')

#     return render(request, 'users/login.html')


# login 2
# login with authentication form
def login_user(request):
    if request.method == 'POST':
        # form = AuthenticationForm(request, data=request.POST)
        form = CustomAuthForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('templates_app:home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        # form = AuthenticationForm()
        form = CustomAuthForm()

    return render(request, 'users\login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect("users:login_user")

# # registration version 1 with default form
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # # version 1
            raw_password = form.cleaned_data["password1"]
            username = form.cleaned_data["username"]
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'You are now logged in.')
                return redirect("templates_app:home")

            # # version 2
            # messages.success(request, 'User Registered Successfully!')
            # return redirect("users:login_user")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})


# # Registration version 2 with custom form
def register_user(request):
    if request.method == "POST":
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Registered Successfully!')
            return redirect("users:login_user")
    else:
        form = CustomUserRegisterForm()

    return render(request, "users/register.html", {"form": form})

from django.contrib.auth import update_session_auth_hash

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()

            # Keeps the user logged in after password change
            # Without this, Django would log the user out
            update_session_auth_hash(request, user)   
            messages.success(request, 'Your password has been updated successfully.')
            return redirect('templates_app:home')
        else:
            messages.error(request, 'Please correct the errors below and try again.')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'users/change_password.html', {'form': form})


from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect

def custom_password_reset_request(request):
    # If form is submitted (POST)
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # Get the email entered in the form
            user_email = form.cleaned_data['email']
            # Get the user(s) associated with this email
            users = form.get_users(user_email)

            for user in users:
                # Generate unique token for password reset
                token = default_token_generator.make_token(user)
                # Encode the user's primary key into base64
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                # Get the current website domain (e.g., localhost:8000)
                domain = get_current_site(request).domain
                # Build the password reset link (URL)
                reset_link = reverse('users:custom_password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
                full_url = f'http://{domain}{reset_link}'

                # Create email content from template
                message = render_to_string('users/password_reset_email.html', {
                    'user': user,
                    'reset_url': full_url
                })

                # Send the password reset email
                send_mail(
                    subject='Reset Your Password',
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                )

            messages.success(request, 'We have sent you an email with a link to reset your password.')
            return redirect('templates_app:home')
    else:
        # If GET request, show empty form
        form = PasswordResetForm()

    return render(request, 'users/password_reset.html', {'form': form})




from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from users.models import CustomUser  

def custom_password_reset_confirm(request, uidb64, token):
    """
    Handles setting the new password after the user clicks the email link.
    """

    try:
        # Decode the user ID from base64
        uid = urlsafe_base64_decode(uidb64).decode()
        # Try to retrieve the user from the database
        user = get_object_or_404(CustomUser, pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    # If the token is valid and the user exists
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            # Bind form with POST data and the current user
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                # Save the new password
                form.save()
                messages.success(request, 'Your password was successfully reset!')
                return redirect('users:login_user')
        else:
            # If GET request, display empty form to set new password
            form = SetPasswordForm(user)

        return render(request, 'users/password_reset_confirm.html', {'form': form})
    else:
        # If the token is invalid or expired
        messages.error(request, 'The reset link is invalid or has expired.')
        return redirect('users:password_reset')
