from django.db import models
from django.utils import timezone

class User(models.Model):
    course_of_interest = models.CharField(max_length=500)
    name=models.CharField(max_length=1000)
    email=models.EmailField(max_length=200)
    gender=models.CharField(max_length=500)
    date_of_birth=models.DateField(max_length=200)
    address=models.CharField(max_length=1000)
    phone_number=models.CharField(max_length=20)
    educational_background=models.CharField(max_length=200)
    occupation=models.CharField(max_length=200)
    learning_mode=models.CharField(max_length=100)
    sponsorship=models.CharField(max_length=50)
    sponsor_relationship=models.CharField(max_length=100, null=True)
    sponsor_phone_number=models.CharField(max_length=20, null=True)
    how_did_you_hear_about_us=models.CharField(max_length=200)
    joined=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name