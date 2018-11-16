from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Asset(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    currentLocation = models.ForeignKey(Location, on_delete=models.CASCADE)
    orgTag = models.CharField(max_length=20)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    manufacturerPartNum = models.IntegerField()
    description = models.CharField(max_length=500)
    dateImplemented = models.DateField()
    maintNotes = models.CharField(max_length=500)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)



