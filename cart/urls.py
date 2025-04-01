from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:coffee_id>/', views.add_to_cart, name='add_to_cart'),
    path('view/', views.view_cart, name='view_cart'),
]