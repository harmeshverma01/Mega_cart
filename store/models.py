from django.db import models
import uuid
# Create your models here.

class Product(models.Model):
    Choice = (
        ('high', 'high'),
        ('medium', 'medium'),
        ('low', 'low'),
    )
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=8, decimal_places=2)
    unique_code = models.UUIDField(default=uuid.uuid1, unique=True)
    Quentity = models.CharField(choices=Choice, max_length=20)
    # Size = models.CharField(choices=size, max_length=20)
    
    def __str__(self):
        return self.Title
    
    
class ProductColor(models.Model):
    colour = (
        ('blue', 'blue'),
        ('red', 'red'),
        ('green', 'green'),
        ('black', 'black')
    )
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='products')
    Colour = models.CharField(choices=colour, max_length=20)
    
class ProductImage(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)   
    image = models.ImageField()
    