from django.shortcuts import render
from .models import Coach


def index(request):
    return render(request, 'coach/index.html')


def coach(request):
    tren = Coach.objects.all()
    context = {
        "coach": tren
    }
    return render(request, "coach/coach.html", context)
