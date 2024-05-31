from django.shortcuts import render
from .models import Tym

def seznam_tymu(request):
    tymy = Tym.objects.all()
    return render(request, 'fotbalovaaplikace/seznam_tymu.html', {'tymy': tymy})
