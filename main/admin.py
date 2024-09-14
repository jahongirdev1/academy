
from django.contrib import admin
from .models import *
class UserModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserModel, UserModelAdmin)



class CourseModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(CourseModel, CourseModelAdmin)



class LessonModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(LessonModel, LessonModelAdmin)