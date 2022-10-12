from django.db import models

from Phone_Book.models import PhoneBook

# Create your models here.

class Citizen(models.Model):
    name_of_citizen = models.CharField(blank=True, null=True, max_length=300, default="")
    sex = models.CharField(blank=True, null=True, max_length=300, default="")
    date_of_birth = models.CharField(blank=True, null=True, max_length=300, default="")
    place_of_birth = models.CharField(blank=True, null=True, max_length=300, default="")
    gps_address = models.CharField(blank=True, null=True, max_length=300, default="")
    phone_number = models.ForeignKey(PhoneBook, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name_of_citizen}'
