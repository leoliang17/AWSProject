from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assets/', views.assets, name='assets'),
    path('employees/', views.employees, name='employees'),
    path('manufacturers/', views.manufacturers, name='manufacturers'),
    path('locations/', views.locations, name='locations'),
    path('createAsset/', views.createAsset, name='createAsset'),
    path('updateAsset/', views.updateAsset, name='updateAsset'),
    path('createEmployee/', views.createEmployee, name='createEmployee'),
    path('updateEmployee/', views.updateEmployee, name='updateEmployee'),
    path('createManufacturer/', views.createManufacturer, name='createManufacturer'),
    path('updateManufacturer/', views.updateManufacturer, name='updateManufacturer'),
    path('createLocation/', views.createLocation, name='createLocation'),
    path('updateLocation/', views.updateLocation, name='updateLocation'),
]