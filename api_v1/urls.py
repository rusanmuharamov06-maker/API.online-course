from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, CourseViewSet, StudentViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]