from django.urls import path
from .views import *
urlpatterns = [
    path('',home),
    path('project/<int:pk>',project),
    path('project2/<int:pk>',project2),
    path('project3/<int:pk>',project3),
]
