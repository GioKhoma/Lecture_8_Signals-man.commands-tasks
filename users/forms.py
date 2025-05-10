from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
# from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()



# class CustomUserRegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', "last_name"]
        
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
#         }



class CustomUserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 
                #   'first_name', "last_name",  
                #   'birthdate', 'phone_number', 'bio',
                  'password1', 'password2',
                  ]
        
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            # 'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            # 'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            # 'birthdate': forms.DateInput(attrs={'class': 'form-control form-control-lg', 'type': 'date'}),
            # 'phone_number': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            # 'bio': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': 4}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
        }


class CustomAuthForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"autofocus": True, 'class': "form-control"})
    )















