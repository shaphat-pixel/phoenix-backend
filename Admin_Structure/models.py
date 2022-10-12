from email.policy import default
from django.db import models
from django.contrib.postgres.fields import ArrayField
from Data_Bank.models import *

# Create your models here.
class Demographics(models.Model):
    name_of_region = models.CharField(null=True, default="", max_length=300)
    employed = models.CharField(null=True, default="", max_length=300)
    unemployed = models.CharField(null=True, default="", max_length=300)
    children = models.CharField(null=True, default="", max_length=300)
    adults = models.CharField(null=True, default="", max_length=300)
    marriage_rate = models.CharField(null=True, default="", max_length=300)
    birth_rate = models.CharField(null=True, default="", max_length=300)
    death_rate = models.CharField(null=True, default="", max_length=300)

    def __str__(self):
        return f'{self.region}'

class Regions(models.Model):
    region_name = models.CharField(null=True, default="", max_length=300)


    def __str__(self):
        return f'{self.region}'

class Region(models.Model):
    name = models.ForeignKey(Regions, on_delete=models.CASCADE, null=True, blank=True)
    capital = models.CharField(null=True, default="", max_length=300)
    cities = ArrayField(models.CharField(max_length=300, null=True), blank=True)
    districts = ArrayField(models.CharField(max_length=300, null=True), blank=True)
    population = models.CharField(null=True, default="", max_length=300)
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE, null =True, blank=True)

    def __str__(self):
        return f'{self.name}'