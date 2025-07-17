from django.shortcuts import render
from .models import Employee
# from .serializers import EmployeeSerializer, EmployeeDetailsSerializer, EmployeeImageSerializer
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
# from rest_framework.exceptions import APIException
from rest_framework import parsers
# from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class EmployeeAPIView(GenericAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_field = 'pk'
    
    # get
    def get(self, request, pk=None):
        emp_objs =self.get_queryset()
        serializer = self.get_serializer(emp_objs, many=True)
        
        return Response({
            'status':status.HTTP_200_OK,
            'data':serializer.data
        })

    # create
    def post(self, request, pk=None):
        serializer = EmployeeSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'error':serializer.errors,
                'message':'Invalid Data'
            })
        serializer.save()
        return Response({
                'status':status.HTTP_200_OK,
            'data':serializer.data 
        })
    
  
    # put
    def put(self, request, pk=None):
        emp_objs =Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(emp_objs, data=request.data, partial=False)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'error':serializer.errors,
                'message':'Invalid Data'
            }) 
        serializer.save()
        return Response({
                'status':status.HTTP_200_OK,
            'data':serializer.data 
        })

# class EmployeeViewSet(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeDetailsSerializer
#     parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    
#     def get_serializer_class(self):
#         if self.action=='list':
#             return EmployeeSerializer
#         if self.action=='create':
#             return EmployeeSerializer
#         elif self.action == 'upload_image':
#             return EmployeeImageSerializer
#         return self.serializer_class
    
#     @action(methods=['POST'], detail=True, url_path='upload-image')
#     def upload_image(self, request, pk=None):
#         emp_objs = self.get_object()
#         serializer = self.get_serializer(emp_objs, data= request.data)
        
#         if not serializer.is_valid():
#             return Response({
#                 'status':status.HTTP_400_BAD_REQUEST,
#                 'message':'Invalid data'
#             })
#         serializer.save()
#         return Response({
#                 'status':status.HTTP_200_OK,
#                 'message':'Upload Image Successfully',
#                 'data':serializer.data
#             })
            
#     # get all emp
#     def list(self, request):
#         try:
#             emp_objs = Employee.objects.all()
#             serializer = self.get_serializer(emp_objs, many= True)
            
#             return Response({
#                 'status':status.HTTP_200_OK,
#                 'data': serializer.data
#                 })
            
#         except Exception as e:
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status_code
#             })
            
            
# # add emp
#     def create(self, request):
#         try:
#             serializer = self.get_serializer(data=request.data)
#             if not serializer.is_valid():
#                 return Response({
#                     'status':status.HTTP_400_BAD_REQUEST,
#                     'message':'Invalid Data'
#                 })
            
#             serializer.save()
            
#             return Response({
#                 'status':status.HTTP_201_CREATED,
#                 'data': serializer.data,
#                 'message':'Employee Added Successfully'
#                 })
            
#         except Exception as e:
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status_code
#             })

# # single employee retrieve
#     def retrieve(self, request, pk):   
#         try:
#             id = pk  
#             if id is not None:
#                 emp_objs =self.get_object() 
#                 serializer = self.get_serializer(emp_objs)
            
#             return Response({
#                 'status':status.HTTP_200_OK,
#                 'data': serializer.data
#                 })
            
#         except Exception as e:
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status_code
#             })


#     def destroy(self, request, pk):
#         try:
#             id = pk
#             emp_objs =self.get_object() 
            
#             return Response({
#                 'status':status.HTTP_200_OK,
#                 'message': 'Employee Deleted Successfully'
#                 })
            
#         except Exception as e:
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status_code
#             })
            
# #update all fields
#     def update(self,request,pk=None):
#         try:
#             emp_objs = self.get_object()
#             serializer = self.get_serializer(emp_objs,data=request.data,partial=False)
#             if not serializer.is_valid():
#                 return Response({
#                 'status':status.HTTP_400_BAD_REQUEST,
#                 'message':'Invalid Data'
#                 })
            
#             serializer.save()
#             return Response({
#                 'status' : status.HTTP_201_CREATED,
#                 'data':serializer.data,
#                 'message':'Employee updated successfully'
#             })
        
#         except Exception as e:
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status_code
#             })
        
#     #update specific  fields
#     def partial_update(self,request,pk=None):
#         try:
#             emp_objs = self.get_object()
#             serializer = self.get_serializer(emp_objs,data=request.data,partial=True)
#             if not serializer.is_valid():
#                 return Response({
#                 'status':status.HTTP_400_BAD_REQUEST,
#                 'message':'Invalid Data'
#                 })
            
#             serializer.save()
#             return Response({
#                 'status' : status.HTTP_201_CREATED,
#                 'data':serializer.data,
#                 'message':'Employee partialy_updated successfully'
#             })
        
#         except Exception as e:
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status_code
#             })