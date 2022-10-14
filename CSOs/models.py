from django.db import models
from Admin_Structure.models import * 
# Create your models here.


class Organization(models.Model):
    org_name = models.CharField(blank=True, null=True, max_length=300, default="")
    region_located = models.ForeignKey(Regions, on_delete=models.CASCADE)
   
    def __str__(self):
        return f'{self.org_name}'