from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Course, StudentCourse
from .serializers import CourseSerializer, StudentCourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'instructor']
    search_fields = ['name', 'instructor', 'category']
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        """Recherche personnalisée de cours"""
        name = request.query_params.get('name', '')
        instructor = request.query_params.get('instructor', '')
        category = request.query_params.get('category', '')
        
        courses = Course.objects.all()
        
        if name:
            courses = courses.filter(name__icontains=name)
        if instructor:
            courses = courses.filter(instructor__icontains=instructor)
        if category:
            courses = courses.filter(category__icontains=category)
            
        serializer = self.get_serializer(courses, many=True)
        return Response(serializer.data)

class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer
    
    def get_queryset(self):
        """Filtrer par student_id si fourni"""
        queryset = StudentCourse.objects.all()
        student_id = self.request.query_params.get('student_id')
        if student_id:
            queryset = queryset.filter(student_id=student_id)
        return queryset
