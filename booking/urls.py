
from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.viewBooking, name='booking'),
  path('new_booking/', views.new_booking, name='new_booking'),
  path('edit_booking/<str:pk>/', views.edit_booking, name='edit_booking'),
  path('delete_booking/<str:pk>/', views.delete_booking, name='delete_booking'),
    
]