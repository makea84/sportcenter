from django.contrib import admin

from .models import Classroom, Course, Participation, Place



admin.site.register(Classroom)
admin.site.register(Course)
admin.site.register(Participation)
admin.site.register(Place)