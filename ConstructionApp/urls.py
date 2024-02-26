
from django.contrib import admin
from django.urls import path
from ConstructionApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name ='index' ),



]
