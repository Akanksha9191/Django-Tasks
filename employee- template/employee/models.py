from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator
# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField(max_length=30)
    emp_age=models.IntegerField(
        validators=[MaxValueValidator(60), MinValueValidator(21)]
    )
    emp_salary=models.IntegerField(
        validators=[MaxLengthValidator(4), MinLengthValidator(6)]
    )
    emp_position=models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return f'{self.emp_name} and {self.emp_position}' 