from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    rating = models.IntegerField(
        validators= [MaxValueValidator(5), MinValueValidator(1)]
    )
    is_bestselling = models.BooleanField(default=True)
    author = models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return f'{self.title} and {self.rating}'