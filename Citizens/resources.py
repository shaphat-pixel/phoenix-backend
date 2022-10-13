from import_export import resources
from . models import *

class CitizenResource(resources.ModelResource):
    class Meta:
        model = Citizen
