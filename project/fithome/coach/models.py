from django.db import models

class Coach(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='coach/images/')
    program = models.CharField(max_length=400)
    courses = models.CharField(max_length=400)

