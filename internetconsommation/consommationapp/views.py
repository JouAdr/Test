from django.shortcuts import render
from .models import InternetConsumption
from django.contrib.auth.models import User

def home(request):
    # users = User.objects.all()
    consommations = InternetConsumption.objects.all()
    consommations_upload = list()
    consommations_download = list()
    consommation_total = list()

    for consommation in consommations:
        consommations_upload.append(consommation.upload)
        consommations_download.append(consommation.download)
    
    for i in range(len(consommations_upload)):
        consommation_total.append(consommations_upload[i] + consommations_download[i])

    return render(request, 'home.html', {'consommations':consommations, 'consommation_total':consommation_total})
