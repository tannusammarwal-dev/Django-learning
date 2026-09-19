from django.db import models

# Create your models here.
class Students(models.Model):
    student_name =models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=50)


    