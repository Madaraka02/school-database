from django.urls import path
from .views import home, teacher_sessions

urlpatterns = [
    path('', home, name="home"),
    path('teacher-session/<int:id>/', teacher_sessions, name="sessions"),
]