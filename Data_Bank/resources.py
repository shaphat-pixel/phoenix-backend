from import_export import resources
from . models import *

class ContinentsResource(resources.ModelResource):
    class Meta:
        model = Continents

class CountriesResource(resources.ModelResource):
    class Meta:
        model = Countries

class CapitalsResource(resources.ModelResource):
    class Meta:
        model = Capitals

class CitiesResource(resources.ModelResource):
    class Meta:
        model = Cities
