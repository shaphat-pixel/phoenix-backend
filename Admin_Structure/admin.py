from django.contrib import admin
from .models import *
# Register your models here.

from import_export.admin import ImportExportModelAdmin


@admin.register(Demographics)
class DemographicsAdmin(ImportExportModelAdmin):
    list_display = ("name_of_region", "employed", "unemployed", "children", "adults", "marriage_rate", "birth_rate", "death_rate" )
    pass


@admin.register(Regions)
class RegionsAdmin(ImportExportModelAdmin):
    list_display = ("region_name",)
    pass

@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin):
    list_display = ("name", "capital", "cities", "districts", "population", "demographics")
    pass
