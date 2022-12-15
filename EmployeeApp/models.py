from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import UserManager

# Create your models here.

class User(AbstractBaseUser):
    
    username=None
    first_name=None
    last_name=None

    emp_id = models.CharField(max_length=5, unique=True)
    emp_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    designation = models.CharField(max_length=100)
    email = models.EmailField(('email address'), unique=True) # changes email to unique and blank to false
    objects = UserManager()

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = []
    

    def __str__(self):
        return self.emp_name