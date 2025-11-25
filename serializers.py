from rest_framework import serializers
from .models import Course, StudentCourse

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'instructor', 'category', 'schedule', 'description', 'created_at']

class StudentCourseSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name', read_only=True)
    
    class Meta:
        model = StudentCourse
        fields = ['id', 'student_id', 'course', 'course_name', 'enrollment_date']