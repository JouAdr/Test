from django.shortcuts import render
from django.http import HttpResponse
from .models import InternetConsumption

def home(request):
    consommations = InternetConsumption.objects.all()
    return render(request, 'home.html', {'consommations':consommations})
