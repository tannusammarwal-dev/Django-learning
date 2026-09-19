from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    age =models.IntegerField()
    email =models.CharField(max_length=100)
    course =models.CharField(max_length=100)
    city = models.CharField(null =True)

    def __str__(self):
        return self.name

