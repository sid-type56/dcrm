from django.db import models
from django.utils import timezone

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
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