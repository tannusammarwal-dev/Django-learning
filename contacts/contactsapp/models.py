from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=50,null=False)
    email =models.CharField(max_length=100)
    message =models.TextField()
    # created_at =models.DateField()

    def __str__(self):
        self.name