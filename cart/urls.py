from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:coffee_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<int:item_id>/', views.update_quantity, name='update_quantity'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]