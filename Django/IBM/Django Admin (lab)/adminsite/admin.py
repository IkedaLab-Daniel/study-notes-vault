from django.contrib import admin
from .models import Course, Instructor, Lesson

# Register your models here.
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]
admin.site.register(Course, CourseAdmin)

class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']
admin.site.register(Instructor, InstructorAdmin)
