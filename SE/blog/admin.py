from django.contrib import admin

from blog.models import Question,Answer,Comments
# Register your models here.
admin.site.register(Question)

admin.site.register(Answer)

admin.site.register(Comments)
