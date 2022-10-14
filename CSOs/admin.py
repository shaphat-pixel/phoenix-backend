from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from CSOs.models import Organization


@admin.register(Organization)
class DemographicsAdmin(ImportExportModelAdmin):
    list_display = ("org_name","region_located",)
    pass

