from django.shortcuts import render


def coach(request):
    return render(request, "coach/coach.html")
