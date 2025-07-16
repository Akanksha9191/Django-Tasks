from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'emp_name', 'position', 'salary']
        read_only_fields = ['id']
        
# class EmployeeDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = EmployeeSerializer.Meta.fields+['image']
#         read_only_fields = ['id']

# class EmployeeImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ['id', 'image']
#         read_only_fields = ['id']