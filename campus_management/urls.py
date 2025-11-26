from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Page d'accueil API
def home(request):
    return JsonResponse({
        "status": "API is running",
        "service": "Courses API",
        "endpoints": {
            "courses": "/api/courses/courses/",
            "enrollments": "/api/courses/enrollments/"
        }
    })

urlpatterns = [
    path('', home),  # Page home
    path('admin/', admin.site.urls),
    path('api/courses/', include('courses.urls')),
]
