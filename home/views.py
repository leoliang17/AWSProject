from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import forms as forms
from . import models as models
from django import forms as djangoForms
from django.contrib.auth import authenticate, login



def index(request):
    context = {}
    return render(request, 'home/index.html', context)

def assets(request):
    assets = models.Asset.objects.all()
    context = {'asset_list': assets,}
    return render(request, 'home/assets.html', context)

def employees(request):
    employees = models.Employee.objects.all()
    context = {'employee_list': employees,}
    return render(request, 'home/employees.html', context)

def manufacturers(request):
    manufacturers = models.Manufacturer.objects.all()
    context = {'manufacturer_list': manufacturers,}
    return render(request, 'home/manufacturers.html', context)

def locations(request):
    locations = models.Location.objects.all()
    context = {'location_list': locations,}
    return render(request, 'home/locations.html', context)

def createAsset(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.CreateAssetForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            asset = models.Asset()
            asset.uniqueIdentifier = form.cleaned_data['uniqueIdentifier']
            asset.currentLocation = form.cleaned_data['currentLocation']
            asset.orgTag = form.cleaned_data['orgTag']
            asset.manufacturer = form.cleaned_data['manufacturer']
            asset.manufacturerPartNum = form.cleaned_data['manufacturerPartNum']
            asset.description = form.cleaned_data['description']
            asset.dateImplemented = form.cleaned_data['dateImplemented']
            asset.maintNotes = form.cleaned_data['maintNotes']
            asset.employee = form.cleaned_data['employee']

            asset.save()

            return HttpResponseRedirect('/home/assets/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.CreateAssetForm()

    context = {'form': form}
    return render(request, 'home/createAsset.html', context)

def updateAsset(request, pk):
    #Employee instance 
    asset = models.Asset.objects.get(pk=pk)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.UpdateAssetForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            asset.uniqueIdentifier = form.cleaned_data['uniqueIdentifier']
            asset.currentLocation = form.cleaned_data['currentLocation']
            asset.orgTag = form.cleaned_data['orgTag']
            asset.manufacturer = form.cleaned_data['manufacturer']
            asset.manufacturerPartNum = form.cleaned_data['manufacturerPartNum']
            asset.description = form.cleaned_data['description']
            asset.dateImplemented = form.cleaned_data['dateImplemented']
            asset.maintNotes = form.cleaned_data['maintNotes']
            asset.employee = form.cleaned_data['employee']

            asset.save()

            return HttpResponseRedirect('/home/assets/')

    # if a GET (or any other method) we'll create a blank form
    else:
        initial_data = djangoForms.model_to_dict(asset)
        form = forms.UpdateAssetForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'home/updateAsset.html', context)

def createEmployee(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.CreateEmployeeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            employee = models.Employee()
            employee.first_name = form.cleaned_data['first_name']
            employee.last_name = form.cleaned_data['last_name']
            employee.position = form.cleaned_data['position']
            employee.location = form.cleaned_data['location']

            employee.save()

            return HttpResponseRedirect('/home/employees/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.CreateEmployeeForm()

    context = {'form': form}
    return render(request, 'home/createEmployee.html', context)

def updateEmployee(request, pk):
    #Employee instance 
    employee = models.Employee.objects.get(pk=pk)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.UpdateEmployeeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            employee.first_name = form.cleaned_data['first_name']
            employee.last_name = form.cleaned_data['last_name']
            employee.position = form.cleaned_data['position']
            employee.location = form.cleaned_data['location']

            employee.save()

            return HttpResponseRedirect('/home/employees/')

    # if a GET (or any other method) we'll create a blank form
    else:
        initial_data = djangoForms.model_to_dict(employee)
        form = forms.UpdateEmployeeForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'home/updateEmployee.html', context)

def createManufacturer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.CreateManufacturerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            manufacturer = models.Manufacturer()
            manufacturer.name = form.cleaned_data['name']
            manufacturer.description = form.cleaned_data['description']

            manufacturer.save()

            return HttpResponseRedirect('/home/manufacturers/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.CreateManufacturerForm()

    context = {'form': form}
    return render(request, 'home/createManufacturer.html', context)

def updateManufacturer(request, pk):
    #Manufacterer instance 
    manufacturer = models.Manufacturer.objects.get(pk=pk)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.UpdateManufacturerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            manufacturer.name = form.cleaned_data['name']
            manufacturer.description = form.cleaned_data['description']

            manufacturer.save()

            return HttpResponseRedirect('/home/manufacturers/')

    # if a GET (or any other method) we'll create a blank form
    else:
        initial_data = djangoForms.model_to_dict(manufacturer)
        form = forms.UpdateManufacturerForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'home/updateManufacturer.html', context)

def createLocation(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.CreateLocationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            location = models.Location()
            location.name = form.cleaned_data['name']
            location.address = form.cleaned_data['address']
            location.city = form.cleaned_data['city']
            location.state = form.cleaned_data['state']
            location.country = form.cleaned_data['country']

            location.save()

            return HttpResponseRedirect('/home/locations/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.CreateLocationForm()

    context = {'form': form}
    return render(request, 'home/createLocation.html', context)

def updateLocation(request, pk):
    #Location instance 
    location = models.Location.objects.get(pk=pk)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.UpdateLocationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            location.name = form.cleaned_data['name']
            location.address = form.cleaned_data['address']
            location.city = form.cleaned_data['city']
            location.state = form.cleaned_data['state']
            location.country = form.cleaned_data['country']

            location.save()

            return HttpResponseRedirect('/home/locations/')

    # if a GET (or any other method) we'll create a blank form
    else:
        # get initial data
        initial_data = djangoForms.model_to_dict(location)
        form = forms.UpdateLocationForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'home/updateLocation.html', context)

def logon(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/home/index/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.LoginForm()
    context = {'form': form}
    return render(request, 'home/login.html', context)
