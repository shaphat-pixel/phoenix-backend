from import_export import resources
from . models import *

class DemographicsResource(resources.ModelResource):
    class Meta:
        model = Demographics

class RegionsResource(resources.ModelResource):
    class Meta:
        model = Regions

class RegionResource(resources.ModelResource):
    class Meta:
        model = Region