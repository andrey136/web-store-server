from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=80) 
    description = models.TextField() 
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    image = models.ImageField(upload_to='products/img')

    def __str__(self):
        return self.title

