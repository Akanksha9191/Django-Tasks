from django.shortcuts import render
from .models import Employee
# Create your views here.
def Index(request):
    employees = Employee.objects.all()
    print(Employee.objects.all())
    return render(request, 'employee/index.html',{
        'employee1':employees
    })
