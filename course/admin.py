from django.contrib import admin
from .models import *


admin.site.register(Course)
admin.site.register(CourseCategory)
admin.site.register(Chapter)
admin.site.register(Task)
admin.site.register(TaskComment)
admin.site.register(CourseComment)
