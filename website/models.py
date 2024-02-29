from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    email=models.EmailField(default='example@example.com')
    first_name = models.CharField(max_length = 50,validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=50,validators=[MinLengthValidator(2)])
    phone = models.CharField(max_length=10,validators=[MinLengthValidator(10)])
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.first_name}{self.last_name}")
    

class MyInterest(models.Model):
    name = models.CharField(max_length=50)
    interest = models.CharField(max_length=100)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"{self.name}{self.interest}")
    
class MyImages(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(null=True,blank=True,upload_to="images/")

    def __str__(self):
        return None 