from email.policy import default
from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Continents(models.Model):
    continent = models.CharField(default="", max_length=300)
    population = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.continent}'


class Countries(models.Model):
    continent = models.ForeignKey(Continents, on_delete=models.CASCADE)
    country = models.CharField(default="", max_length=300)
    population = models.PositiveIntegerField(null=True)
    languages = models.CharField(default="", blank=True, max_length=300)

    def __str__(self):
        return f'{self.country}'


class Capitals(models.Model):
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    regions = ArrayField(models.CharField(max_length=300, null=True), blank=True)
    capital = models.CharField(default="", max_length=300)
    population = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.capital}'

class Cities(models.Model):
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    city = models.CharField(default="", max_length=300)
    population = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.city}'

