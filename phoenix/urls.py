
from django.contrib import admin
from django.urls import path
from Data_Bank import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('continents-list',views.ContinentList,name="continents-list"),
]
