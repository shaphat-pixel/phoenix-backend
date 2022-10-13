from import_export import resources
from . models import *

class Gov_MinistriesResource(resources.ModelResource):
    class Meta:
        model = Gov_Ministries

class State_institutionsResource(resources.ModelResource):
    class Meta:
        model = State_institutions

class State_owned_enterprisesResource(resources.ModelResource):
    class Meta:
        model = State_owned_enterprises

class Electoral_AreaResource(resources.ModelResource):
    class Meta:
        model = Electoral_Area

class Political_PartiesResource(resources.ModelResource):
    class Meta:
        model = Political_Parties

class Party_ExecutivesResource(resources.ModelResource):
    class Meta:
        model = Party_Executives

class Polling_StationsResource(resources.ModelResource):
    class Meta:
        model = Polling_Stations

class MPResource(resources.ModelResource):
    class Meta:
        model = MP

class Election_ResultsResource(resources.ModelResource):
    class Meta:
        model = Election_Results

