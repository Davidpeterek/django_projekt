from django.shortcuts import render
from .models import Tym, Hrac, Zapas

def home(request):
    return render(request, 'fotbal/uvod.html')

def seznam_tymu(request):
    tymy = Tym.objects.all()
    return render(request, 'fotbal/seznam_tymu.html', {'tymy': tymy})
