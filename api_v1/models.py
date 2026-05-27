from django.db import models

class Teacher(models.Model):
    """Преподаватель"""
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200, blank=True)
    experience = models.IntegerField(default=0, verbose_name="Опыт (лет)")
    
    def __str__(self):
        return self.name

class Course(models.Model):
    """Курс"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(default=10, verbose_name="Часов")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Student(models.Model):
    """Студент"""
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name='students', blank=True)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    """Отзыв"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    rating = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.rating}/5 - {self.course.title}"