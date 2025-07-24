from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
   
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default='customer')

    roles = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default='user')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    age = models.IntegerField()
    bio = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)    # Required
    is_staff = models.BooleanField(default=False)    # Required

    objects = UserManager()

    USERNAME_FIELD = 'email'         # Required: what field is used as username
    REQUIRED_FIELDS = ['name', 'age']  # Required when creating superusers

    def __str__(self):
        return self.email
