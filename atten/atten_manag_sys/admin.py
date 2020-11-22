from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(teacher_user)
admin.site.register(student_user)
admin.site.register(communication_student)
admin.site.register(leave)
admin.site.register(Faculty)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(SubjectAttendenceTable)
