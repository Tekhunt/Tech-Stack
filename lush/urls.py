from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('create/', createTask, name='create'),
    path('get/', getTask, name='create'),
    path('details/<str:pk>/', details, name='create'),
    path('update/<str:pk>/', updateTask, name='create'),
    path('delete/<str:pk>/', deleteTask, name='create'),

]