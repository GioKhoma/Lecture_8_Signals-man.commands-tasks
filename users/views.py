from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserRegisterForm, CustomAuthForm


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
