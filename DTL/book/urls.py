from django.urls import path
from . import views
urlpatterns = [
   path('', views.index),
   # path('bookdetail', views.February),
   path('<int:id>', views.book_details)
]
