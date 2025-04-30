from django import forms
from .models import Employee

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Your Name",
        widget=forms.TextInput(attrs={
            'class': "form-control",
            "placeholder": "Enter your full name"
        })
    )

    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={
            'class': "form-control",
            "placeholder": "Enter your email"
        })
    )

    message = forms.CharField(
        max_length=300,
        label="Your Message",
        required=False,
        widget=forms.Textarea(attrs={
            'class': "form-control",
            "placeholder": "Write your message here",
            'rows': 5
        })
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith(".scsa"):
            raise forms.ValidationError("Only .scsa email addresses are allowed.")
        return email


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["first_name", "last_name", "email", "position"]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email address'
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Job title or position'
            }),
        }