from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin


@admin.register(Gov_Ministries)
class Gov_MinistriesAdmin(ImportExportModelAdmin):
    list_display = ("ministry_name",)
    pass

@admin.register(State_institutions)
class State_institutionsAdmin(ImportExportModelAdmin):
    list_display = ("enterprise_region", "inst_name", "directors",)
    pass

@admin.register(State_owned_enterprises)
class State_owned_enterprisesAdmin(ImportExportModelAdmin):
    list_display = ("enterprise_region", "enterprise_name", "directors",)
    pass

@admin.register(Constituencies)
class ConstituenciesAdmin(ImportExportModelAdmin):
    list_display = ("const_region", "const_name",)
    pass

@admin.register(Electoral_Area)
class Electoral_AreaAdmin(ImportExportModelAdmin):
    list_display = ("elec_area_const", "elec_area_name",)
    pass


@admin.register(Political_Parties)
class Political_PartiesAdmin(ImportExportModelAdmin):
    list_display = ("party_name",)
    pass

@admin.register(Party_Executives)
class Party_ExecutivesAdmin(ImportExportModelAdmin):
    list_display = ("party_of_executive", "name_of_executive", "tenure",)
    pass

@admin.register(Polling_Stations)
class Polling_StationsAdmin(ImportExportModelAdmin):
    list_display = ("polling_region", "electoral_area", "polling_const", "polling_name",)
    pass

@admin.register(MP)
class MPAdmin(ImportExportModelAdmin):
    list_display = ("mp_name", "const_name", "tenure", "mp_party_name",)
    pass

@admin.register(Election_Results)
class Election_ResultsAdmin(ImportExportModelAdmin):
    list_display = ("results_polling_station", "name_of_party", "year_of_election", "pres_candidate", "pres_candidate_results", "parl_candidate", "parl_candidate_results",)
    pass




