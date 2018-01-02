from django.contrib import admin
from .models import Faculty,Student,Course,Language,Assignment, Question, Answer, Comments

admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Language)
admin.site.register(Assignment)

admin.site.register(Question)

admin.site.register(Answer)

admin.site.register(Comments)
