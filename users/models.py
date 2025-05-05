from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set', 
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  
        blank=True
    )

    def __str__(self):
        return self.username



# # users/models.py
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         """
#         Create and return a user with an email and password.
#         """
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         """
#         Create and return a superuser with an email, password, and admin rights.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)  # Email as the unique identifier
#     birthdate = models.DateField(null=True, blank=True)
#     phone_number = models.CharField(max_length=15, null=True, blank=True)
#     bio = models.TextField(null=True, blank=True)

#     # Add required fields for user authentication
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)  # Required for admin access
#     date_joined = models.DateTimeField(auto_now_add=True)

#     USERNAME_FIELD = 'email'  # Set email as the unique identifier
#     REQUIRED_FIELDS = []  # No username required, only email and password

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email


