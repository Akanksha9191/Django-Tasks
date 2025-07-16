from django.db import models

# Create your models here.
def employee_image_file_path(instance, filename):
    return '/'.join([str(instance.emp_name), filename])

class Employee(models.Model):
    emp_name = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    salary = models.IntegerField()
    image = models.ImageField(upload_to=employee_image_file_path, null=True, blank=True)
    
    def __str__(self):
        return self.emp_name
