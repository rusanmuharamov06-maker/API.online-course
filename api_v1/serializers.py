from rest_framework import serializers
from .models import Teacher, Course, Student, Review

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'specialization', 'experience']

class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='teacher', write_only=True
    )
    
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'duration', 'teacher', 'teacher_id', 'created_at']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'courses']

class ReviewSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source='course', write_only=True
    )
    student = serializers.StringRelatedField(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student', write_only=True, required=False, allow_null=True
    )
    
    class Meta:
        model = Review
        fields = ['id', 'course', 'course_id', 'student', 'student_id', 'rating', 'text', 'created_at']