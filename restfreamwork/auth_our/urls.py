from django.contrib import admin
from django.urls import path,include
from .views import *



urlpatterns = [
    path('',home),
    path('add_car/',add_car),
    path('get_cars/',get_cars),
    path('cars/<int:pk>/', cars),
    path('carsX',Car_view.as_view(),name='carsx'),
    path('car/<int:pk>/',CarX.as_view(),name='cars3')
]
