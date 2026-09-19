from django.shortcuts import render
from .models import Students
# Create your views here.


def student(request):
    student_data = Students.objects.first()
    return render(request ,'studentdata/student.html',{'student_data':student_data})