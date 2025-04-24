from django.shortcuts import render

def home(request):
    message = {
        'type': 'success',  # could be 'success', 'warning', or 'error'
        'title': 'Welcome Back!',
        'text': 'You have successfully logged in.'
    }
    return render(request, 'templates_app/home.html', {
        'user_name': 'Giorgi',
        'is_admin': True,
        'message': message
    })

def about(request):
    return render(request, 'templates_app/about.html')

def posts(request):
    sample_posts = [
        {'title': 'First Post', 'date': '2025-04-01'},
        {'title': 'Second Post', 'date': '2025-04-15'},
    ]
    return render(request, 'templates_app/posts.html', {'posts': sample_posts})

from .models import Profile

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'templates_app/profiles.html', {'profiles': profiles})
