# Register your models here.
from django.contrib import admin

from mainapp.models import Courses, CourseTeachers, Lesson, News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

admin.site.register(News)
admin.site.register(Courses)
admin.site.register(Lesson)
admin.site.register(CourseTeachers)