from django.db import models

# Create your models here.

class PhoneBook(models.Model):
    contact_name = models.CharField(blank=True, null=True, max_length=300, default="")
    phone_number = models.CharField(blank=True, null=True, max_length=300, default="")
    network = models.CharField(blank=True, null=True, max_length=300, default="")
    IMEI = models.CharField(blank=True, null=True, max_length=300, default="")
    status = models.BooleanField(null=True, blank=True)


    def __str__(self):
        return f'{self.contact_name}'
