from django.shortcuts import render, redirect
from .models import Programs, Exercise


def program(request):
    context = {
        'title': "FitHome - Тренировки",
        'categories': Programs.objects.all(),
        'exercies': Exercise.objects.all()
    }
    return render(request, 'programs/program.html', context)


def workouts(request):
    ...
