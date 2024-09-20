from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.login, name='login'),
    path('login/<str:id>', views.detail, name='detail'),
]