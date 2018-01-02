from django.contrib import admin
from .models import Courses
from .models import Course_details, Syllabus, Faculty, Assignment, Book, Paper
admin.site.register(Courses)
admin.site.register(Course_details)
admin.site.register(Syllabus)
admin.site.register(Faculty)
admin.site.register(Assignment)
admin.site.register(Book)
admin.site.register(Paper)


# Register your models here.
