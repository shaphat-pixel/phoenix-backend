from import_export import resources
from . models import *

class Inst_CategoriesResource(resources.ModelResource):
    class Meta:
        model = Inst_Categories


class InstitutionResources(resources.ModelResource):
    class Meta:
        model = Institution