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
