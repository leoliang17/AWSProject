from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)

class Asset(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    currentLocation = models.CharField(max_length=100)
    orgTag = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=30)
    manufacturerPartNum = models.IntegerField()
    description = models.CharField(max_length=500)
    dateImplemented = models.DateField()
    maintNotes = models.CharField(max_length=500)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
