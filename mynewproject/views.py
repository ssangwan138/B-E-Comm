from msilib.schema import ComboBox
from django.shortcuts import render
from django.http import HttpResponse
from math import ceil 

def index(request):
    return render(request, 'index.html')


