from import_export import resources
from . models import *

class OrganizationResource(resources.ModelResource):
    class Meta:
        model = Organization
