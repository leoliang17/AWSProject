from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assets/', views.assets, name='assets'),
    path('employees/', views.employees, name='employees'),
    path('manufacturers/', views.manufacturers, name='manufacturers'),
    path('locations/'), views.locations, name='locations'.
]