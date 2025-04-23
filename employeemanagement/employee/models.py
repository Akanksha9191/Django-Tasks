from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField(max_length=30)
    emp_age=models.IntegerField()
    emp_salary=models.IntegerField()
    emp_position=models.CharField(max_length=20)