from django.urls import path, include
# from .views import EmployeeViewSet
# from rest_framework.routers import DefaultRouter
from .views import EmployeeAPIView
# router = DefaultRouter()
# router.register('', EmployeeViewSet, basename='Employee')
# app_name = 'employee'

# urlpatterns = [
#     path('', include(router.urls))
# ]
from .views import EmployeeAPIView
app_name ='employee'
urlpatterns = [
    path('',EmployeeAPIView.as_view()),
    path('<int:pk>', EmployeeAPIView.as_view())
    
]

   