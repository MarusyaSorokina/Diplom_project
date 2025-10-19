from django.contrib import admin
from .models import Programs, Exercise, Photo


class PhotoAdd(admin.StackedInline):
    model = Photo
    fields = ('exercise', 'add_photo')
    extra = 0

class ExerciseAdmin(admin.ModelAdmin):
    inlines = [PhotoAdd]

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'add_photo')

admin.site.register(Programs)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Photo, PhotoAdmin)



