from django.urls import path
from .import views
urlpatterns = [
    path('jan', views.January),
    path('feb', views.February),
    path('march', views.March),
    path('april', views.April),
    path('may', views.May)
    
]
# 8000/month/jan
# anglebraket