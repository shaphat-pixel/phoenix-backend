from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
from rest_framework.decorators import api_view
from uritemplate import partial
from .serializers import *
from . models import *
# Create your views here.



@api_view(['GET'])
def ContinentList(request):
    continents = Continents.objects.all()
    serializer = ContinentsSerializer(continents, many=True)
    return Response(serializer.data)