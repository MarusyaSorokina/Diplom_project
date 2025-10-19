from django.db import models

class Programs(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Программа')
    description = models.TextField(blank=True, verbose_name='Описание программы')



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'программу'
        verbose_name_plural = 'программы'

class Exercise(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название упражения')
    image = models.ImageField(upload_to='programs/images/', blank=True, verbose_name='Изображение')
    url = models.URLField(blank=True, unique=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    short_description = models.CharField(max_length=100, blank=True, verbose_name='Краткое описание')
    category = models.ForeignKey(Programs, on_delete=models.CASCADE, verbose_name='Программа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'упражнение'
        verbose_name_plural = 'упражнения'

class Photo(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, verbose_name='Упражнения')
    add_photo = models.ImageField(upload_to='programs/images/', blank=True, verbose_name='Фото')

    def __str__(self):
        return str(self.id)


    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'