from django.urls import path
from . import views

urlpatterns = [
    path('program/', views.program, name='program'),
    path('workouts', views.workouts, name='workouts'),

]