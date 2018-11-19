from django.urls import path

from . import views

urlpatterns = [
    path('', views.logon, name='logon'),
    path('logon/', views.logon, name='logon'),
    path('index/', views.index, name='index'),
    path('assets/', views.assets, name='assets'),
    path('employees/', views.employees, name='employees'),
    path('manufacturers/', views.manufacturers, name='manufacturers'),
    path('locations/', views.locations, name='locations'),
    path('createAsset/', views.createAsset, name='createAsset'),
    path('updateAsset/<pk>', views.updateAsset, name='updateAsset'),
    path('createEmployee/', views.createEmployee, name='createEmployee'),
    path('updateEmployee/<pk>', views.updateEmployee, name='updateEmployee'),
    path('createManufacturer/', views.createManufacturer, name='createManufacturer'),
    path('updateManufacturer/<pk>', views.updateManufacturer, name='updateManufacturer'),
    path('createLocation/', views.createLocation, name='createLocation'),
    path('updateLocation/<pk>', views.updateLocation, name='updateLocation'),
    path('submitAssetRequest/', views.submitAssetRequest, name='submitAssetRequest'),
    path('deleteAsset/<pk>', views.deleteAsset, name='deleteAsset'),
    path('deleteEmployee/<pk>', views.deleteEmployee, name='deleteEmployee'),
    path('deleteLocation/<pk>', views.deleteLocation, name='deleteLocation'),
    path('deleteManufacturer/<pk>', views.deleteManufacturer, name='deleteManufacturer'),
    path('logoff/', views.logoff, name='logoff'),

]