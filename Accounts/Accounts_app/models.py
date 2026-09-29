from django.db import models

# Create your models here.
class Product(models.Model):
    image =models.ImageField(upload_to='products/')
    name =models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description  = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name