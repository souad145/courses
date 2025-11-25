from django.contrib import admin
from .models import Course, StudentCourse

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'instructor', 'category', 'schedule']
    list_filter = ['category', 'instructor']
    search_fields = ['name', 'instructor']
    ordering = ['name']

@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'course', 'enrollment_date']
    list_filter = ['course', 'enrollment_date']
    search_fields = ['student_id']