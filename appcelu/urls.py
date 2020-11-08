from django.urls import path
from . import views

urlpatterns = [
    path('celulares/', views.Home, name='Home')
]
