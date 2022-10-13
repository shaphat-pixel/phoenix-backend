from django.contrib import admin

from Citizens.models import Citizen
from import_export.admin import ImportExportModelAdmin


@admin.register(Citizen)
class CitizenAdmin(ImportExportModelAdmin):
    list_display = ("name_of_citizen", "sex", "date_of_birth", "place_of_birth", "gps_address", "phone_number",)
    pass

