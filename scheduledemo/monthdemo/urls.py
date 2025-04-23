from django.urls import path
from .import views

urlpatterns = [
    path('<int:monthdemo>', views.monthdemo_schedule),
    path('<str:monthdemo>', views.monthdemo_schedule, name='monthdemo-url')
]