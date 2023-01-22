from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    customer = models.OneToOneField(User,on_delete=models.CASCADE)
    idno = models.IntegerField(blank=False)
    branch = models.CharField(max_length=256, blank=False)
    is_customer = models.BooleanField(default=True)

    def __str__(self):
        return self.customer.username

class Developer(models.Model):
    developer = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=256, blank=False)
    phone = models.IntegerField()
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.developer.username
