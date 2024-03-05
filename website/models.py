from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
from roles import Role
import os
from dotenv import load_dotenv
from django.contrib.auth.hashers import make_password , check_password
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import AbstractUser

load_dotenv()

# Create your models here.

class WebUser(AbstractUser):
    pass

# class UserAuth(models.Model):
#     user = models.OneToOneField(WebUser,on_delete=models.CASCADE)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)

#     def __str__(self):
#         return self.email
    
#     def set_password(self,raw_password):
#         self.password = make_password(raw_password)
#         return None
    
#     def check_password(self,raw_password):
#         return check_password(raw_password,self.password)


# class MyInterest(models.Model):
#     name = models.CharField(max_length=50)
#     interest = models.CharField(max_length=100)
#     created_at=models.DateTimeField(default=timezone.now)
#     updated_at=models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return (f"{self.name}{self.interest}")
    
# class MyImages(models.Model):
#     name=models.CharField(max_length=50)
#     image=models.ImageField(null=True,blank=True,upload_to="images/")

#     def __str__(self):
#         return None 