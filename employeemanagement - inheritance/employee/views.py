from django.shortcuts import render
from .models import Employee
from django.http import Http404
# Create your views here.
def Index(request):
    employees = Employee.objects.all()   #stores all the values in a list
    print(employees)
    return render(request, 'employee/index.html',{'employees':employees})

def employee_details(request, id):
    try:
        employee = Employee.objects.get(pk=id)  
        return render(request, 'employee/employeedetail.html', {
            'emp_name':employee.emp_name,
            'emp_position':employee.emp_position
        })
        
    except:
        raise Http404()
