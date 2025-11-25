from django.db import models

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('informatique', 'Informatique'),
        ('mathematiques', 'Mathématiques'),
        ('physique', 'Physique'),
        ('chimie', 'Chimie'),
        ('biologie', 'Biologie'),
        ('commerce', 'Commerce'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="Nom du cours")
    instructor = models.CharField(max_length=100, verbose_name="Instructeur")
    category = models.CharField(
        max_length=50, 
        choices=CATEGORY_CHOICES, 
        default='informatique',
        verbose_name="Catégorie"
    )
    schedule = models.CharField(max_length=100, verbose_name="Horaire")
    description = models.TextField(blank=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.instructor}"

class StudentCourse(models.Model):
    student_id = models.IntegerField(verbose_name="ID de l'étudiant")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Cours")
    enrollment_date = models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")
    
    class Meta:
        unique_together = ['student_id', 'course']
        verbose_name = "Inscription étudiant"
        verbose_name_plural = "Inscriptions étudiants"
    
    def __str__(self):
        return f"Étudiant {self.student_id} - {self.course.name}"