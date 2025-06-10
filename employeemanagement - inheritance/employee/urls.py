from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index),
    path('<int:id>', views.employee_details, name='employeedetails-url')
]