from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


# Custom user manager: required when creating a custom user model
class CustomUserManager(BaseUserManager):
    """
    Custom user manager where email is used as the unique identifier
    instead of the default username.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a regular user with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')  # Prevent user creation without email

        email = self.normalize_email(email)  # Lowercase + clean the email
        user = self.model(email=email, **extra_fields)  # Create user instance, not yet saved
        user.set_password(password)  # Hash the password securely
        user.save(using=self._db)  # Save to the database
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser (admin) with the given email and password.
        """
        # Ensure these flags are set for superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Double-check to avoid accidental misconfiguration
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)  # Reuse create_user


# Custom user model definition
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that replaces the default Django user model.
    Uses email as the login identifier instead of username.
    """
    # Main login field
    email = models.EmailField('email address', unique=True)

    # Optional personal information
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    # Additional fields
    birthdate = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    cv = models.FileField(upload_to='csv/', null=True, blank=True)

    # Required status fields
    is_active = models.BooleanField(default=True)  # Can login or not
    is_staff = models.BooleanField(default=False)  # Can access admin panel

    # Track when user was created
    date_joined = models.DateTimeField(default=timezone.now)

    # Tell Django to use the custom manager
    objects = CustomUserManager()

    # Use email instead of username to login
    USERNAME_FIELD = 'email'

    # Required when creating a superuser via command line
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email



