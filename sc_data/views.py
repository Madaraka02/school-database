from django.shortcuts import render
from .models import Schedule, Teacher, Session, Class

# Create your views here.

def home(request):
    schedule = Schedule.objects.all()
    teacher = Teacher.objects.all()
    

    context = {
        'schedule':schedule,
        'teacher':teacher
    }
    return render(request, 'home.html', context)

def teacher_sessions(request, id):
    teacher = Teacher.objects.filter(id=id)
    session = Session.objects.filter(teacher__in=teacher)
    classes = Class.objects.filter(teacher__in=teacher)
    

    context = {
        'teacher':teacher,
        'session':session,
        'classes':classes
    }
    return render(request, 'teacherses.html', context)    