from django.urls import path
from .import views

urlpatterns = [
    path('<int:seasondemo>', views.season_schedule),
    path('<str:seasondemo>', views.season_schedule, name='seasondemo-url')
]