from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from Education.models import Inst_Categories, Institution


@admin.register(Inst_Categories)
class Inst_CategoriesAdmin(ImportExportModelAdmin):
    list_display = ("cat_name",)
    pass


@admin.register(Institution)
class InstitutionAdmin(ImportExportModelAdmin):
    list_display = ("inst_cat", "inst_name",)
    pass

