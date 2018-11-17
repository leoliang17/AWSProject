from django import forms
from . import models as models



class CreateLocationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    address = forms.CharField(label='Address', max_length=100, required=False)
    city = forms.CharField(label='City', max_length=100, required=False)
    state = forms.CharField(label='State', max_length=50, required=False)
    country = forms.CharField(label='Country', max_length=100, required=False)

class CreateManufacturerForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    description = forms.CharField(label='Description', max_length=100, required=False)

class CreateEmployeeForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=30, required=True)
    last_name = forms.CharField(label='Last Name', max_length=30, required=True)
    position = forms.CharField(label='Postion', max_length=30, required=True)
    location = forms.ModelChoiceField(label='Location',queryset=models.Location.objects.all(), required=True, to_field_name="id")

class CreateAssetForm(forms.Form):
    id = forms.CharField(label='ID', max_length=10, required=True)
    currentLocation = forms.ModelChoiceField(label='Current Location',queryset=models.Location.objects.all(), required=True, to_field_name="id")
    orgTag = forms.CharField(label='Organization Tag', required=True)
    manufacturer = forms.ModelChoiceField(label='Manufacturer',queryset=models.Manufacturer.objects.all(), required=True, to_field_name="id")
    manufacturerPartNum = forms.DecimalField(label='Manufacturer Part Number', required=True)
    description = forms.CharField(label='Description', required=True)
    dateImplemented = forms.DateField(label='Date Implemented', required=True)
    maintNotes = forms.CharField(label='Maintenance Notes', required=True)
    employee = forms.ModelChoiceField(label='Employee',queryset=models.Employee.objects.all(), required=True, to_field_name="id")

class UpdateLocationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    address = forms.CharField(label='Address', max_length=100, required=False)
    city = forms.CharField(label='City', max_length=100, required=False)
    state = forms.CharField(label='State', max_length=50, required=False)
    country = forms.CharField(label='Country', max_length=100, required=False)

class UpdateManufacturerForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    description = forms.CharField(label='Description', max_length=100, required=False)

class UpdateEmployeeForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=30, required=True)
    last_name = forms.CharField(label='Last Name', max_length=30, required=True)
    position = forms.CharField(label='Postion', max_length=30, required=True)
    location = forms.ModelChoiceField(label='Location',queryset=models.Location.objects.all(), required=True, to_field_name="id")

class UpdateAssetForm(forms.Form):
    id = forms.CharField(label='ID', max_length=10, required=True)
    currentLocation = forms.ModelChoiceField(label='Current Location',queryset=models.Location.objects.all(), required=True, to_field_name="id")
    orgTag = forms.CharField(label='Organization Tag', required=True)
    manufacturer = forms.ModelChoiceField(label='Manufacturer',queryset=models.Manufacturer.objects.all(), required=True, to_field_name="id")
    manufacturerPartNum = forms.DecimalField(label='Manufacturer Part Number', required=True)
    description = forms.CharField(label='Description', required=True)
    dateImplemented = forms.DateField(label='Date Implemented', required=True)
    maintNotes = forms.CharField(label='Maintenance Notes', required=True)
    employee = forms.ModelChoiceField(label='Employee',queryset=models.Employee.objects.all(), required=True, to_field_name="id")



