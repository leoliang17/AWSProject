from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'home/index.html', context)

def assets(request):
    context = {}
    return render(request, 'home/assets.html', context)

def employees(request):
    context = {}
    return render(request, 'home/employees.html', context)

def manufacturers(request):
    context = {}
    return render(request, 'home/manufacturers.html', context)

def locations(request):
    context = {}
    return render(request, 'home/locations.html', context)

def createAsset(request):
    context = {}
    return render(request, 'home/createAsset.html', context)

def updateAsset(request):
    context = {}
    return render(request, 'home/updateAsset.html', context)

def createEmployee(request):
    context = {}
    return render(request, 'home/createEmployee.html', context)

def updateEmployee(request):
    context = {}
    return render(request, 'home/updateEmployee.html', context)

def createManufacturer(request):
    context = {}
    return render(request, 'home/createManufacturer.html', context)

def updateManufacturer(request):
    context = {}
    return render(request, 'home/updateManufacturer.html', context)

def createLocation(request):
    context = {}
    return render(request, 'home/createLocation.html', context)

def updateLocation(request):
    context = {}
    return render(request, 'home/updateLocation.html', context)