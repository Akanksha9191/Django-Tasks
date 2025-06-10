from django.urls import path
from . import views
urlpatterns = [
   path('', views.January),
   path('bookdetail', views.February)
]
