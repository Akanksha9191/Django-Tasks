from django.urls import path
from .import views

urlpatterns = [
    path('<int:weekdemo>', views.week_schedule),
    path('<str:weekdemo>', views.week_schedule, name='weekdemo-url'),
]