from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from .models import InternetConsumption

def home(request): 
    consommations = InternetConsumption.objects.all()
    return render(request, 'home.html', {'consommations':consommations})



def user_details(request, pk):
    try:
        user = User.objects.get(pk=pk)
        consommations = InternetConsumption.objects.all()
        consommations_total = list()

        for consommation in consommations:
            consommations_total.append([consommation.user.username, (consommation.upload + consommation.download)])

    except User.DoesNotExist:
        raise Http404    
    return render(request, 'user_details.html', {'consommations':consommations, 'user':user, 'consommations_total':consommations_total})