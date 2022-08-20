from django.shortcuts import render
from .models import *

def glavnaya(request):
    glavnaya = Glavnaya.objects.all()
    return render(request, 'school/glavnaya.html', {'glavnaya': glavnaya})

def novosti(request):
    novosti = Novosti.objects.all()
    return render (request, 'school/novosti.html', {'novosti': novosti})

def oshkole(request):
    oshkole = Oshkole.objects.all()
    return render (request, 'school/oshkole.html', {'oshkole': oshkole})

def roditelyam(request):
    roditelyam = Roditelyam.objects.all()
    return render (request, 'school/roditelyam.html', {'roditelyam': roditelyam})

def uchebnayadeyatelnost(request):
    uchebnayadeyatelnost = Uchebnayadeyatelnost.objects.all()
    return render (request, 'school/uchebnayadeyatelnost.html', {'uchebnayadeyatelnost': uchebnayadeyatelnost})

def kontakty(request):
    kontakty = Kontakty.objects.all()
    return render (request, 'school/kontakty.html', {'kontakty': kontakty})