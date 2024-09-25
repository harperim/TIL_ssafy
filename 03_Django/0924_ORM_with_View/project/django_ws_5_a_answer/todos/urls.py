from django.urls import path
from . import views


app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('create_todo_ok/', views.create_todo_ok, name='create_todo_ok'),
    path('<int:pk>/', views.detail, name='detail'),
]