from django.db import models

# Create your models here.

class Product(models.Model):
    product_name =models.CharField(max_length=100)
    # p_desc = models.CharField(max_length=100)

# present data representable form



