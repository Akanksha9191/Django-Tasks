from django.shortcuts import render
from .models import Employee

# Create your views here.
def Emp(request):
    employee1 = Employee.objects.all()
    print(employee1)
    return render(request, 'employee/index.html',{'employee1':employee1})
