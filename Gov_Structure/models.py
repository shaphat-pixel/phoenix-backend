
from django.db import models
from Admin_Structure.models import *
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Gov_Ministries(models.Model):
    ministry_name = models.CharField(blank=True, null=True, max_length=300, default="")


    def __str__(self):
        return f'{self.ministry_name}'


class State_institutions(models.Model):
    enterprise_region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    inst_name = models.CharField(blank=True, null=True, max_length=300, default="")
    directors = ArrayField(models.CharField(max_length=300, null=True), blank=True)

    def __str__(self):
        return f'{self.inst_name}'


class State_owned_enterprises(models.Model):
    enterprise_region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    enterprise_name = models.CharField(blank=True, null=True, max_length=300, default="")
    directors = ArrayField(models.CharField(max_length=300, null=True), blank=True)

    def __str__(self):
        return f'{self.enterprise_name}'

class Constituencies(models.Model):
    const_region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    const_name = models.CharField(blank=True, null=True, max_length=300, default="")

    def __str__(self):
        return f'{self.const_name}'


class Electoral_Area(models.Model):
    elec_area_const = models.ForeignKey(Constituencies, on_delete=models.CASCADE)
    elec_area_name = models.CharField(blank=True, null=True, max_length=300, default="")


    def __str__(self):
        return f'{self.elec_area_name}'

class Political_Parties(models.Model):
    party_name = models.CharField(blank=True, null=True, max_length=300, default="")

    def __str__(self):
        return f'{self.party_name}'


class Party_Executives(models.Model):
    party_of_executive = models.ForeignKey(Political_Parties, on_delete=models.CASCADE)
    name_of_executive = models.CharField(blank=True, null=True, max_length=300, default="")
    tenure = models.CharField(blank=True, null=True, max_length=300, default="")

    def __str__(self):
        return f'{self.name_of_executive}'


class Polling_Stations(models.Model):
    polling_region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    electoral_area = models.ForeignKey(Electoral_Area, on_delete=models.CASCADE)
    polling_const = models.ForeignKey(Constituencies, on_delete=models.CASCADE)
    polling_name = models.CharField(blank=True, null=True, max_length=300, default="")

    def __str__(self):
        return f'{self.polling_name}'

class MP(models.Model):
    mp_name = models.CharField(blank=True, null=True, max_length=300, default="")
    const_name = models.ForeignKey(Constituencies, on_delete=models.CASCADE)
    tenure = models.CharField(blank=True, null=True, max_length=300, default="")
    mp_party_name = models.ForeignKey(Political_Parties, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.mp_name}'

class Election_Results(models.Model):
    results_polling_station = models.ForeignKey(Polling_Stations, on_delete=models.CASCADE)
    name_of_party = models.ForeignKey(Political_Parties, on_delete=models.CASCADE)
    year_of_election = models.CharField(blank=True, null=True, max_length=300, default="")
    pres_candidate = models.CharField(blank=True, null=True, max_length=300, default="")
    pres_candidate_results = models.CharField(blank=True, null=True, max_length=300, default="")
    parl_candidate = models.CharField(blank=True, null=True, max_length=300, default="")
    parl_candidate_results = models.CharField(blank=True, null=True, max_length=300, default="")


    def __str__(self):
        return f'{self.year_of_election}'
