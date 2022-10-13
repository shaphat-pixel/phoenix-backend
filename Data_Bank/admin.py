from django.contrib import admin

from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Continents)
class ContinentsAdmin(ImportExportModelAdmin):
    list_display = ("continent", "population",)
    pass


@admin.register(Countries)
class ContinentsAdmin(ImportExportModelAdmin):
    list_display = ("continent", "country", "population", "languages")
    pass

@admin.register(Capitals)
class ContinentsAdmin(ImportExportModelAdmin):
    list_display = ("country", "regions", "capital", "population")
    pass


@admin.register(Cities)
class ContinentsAdmin(ImportExportModelAdmin):
    list_display = ("country", "city", "population",)
    pass

