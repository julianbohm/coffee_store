from django.urls import path
from . import views

urlpatterns = [
    path('', views.coffee_list, name='coffee_list'),
    path('<int:pk>/', views.coffee_detail, name='coffee_detail'),
    path('add/', views.coffee_create, name='coffee_create'),
    path('<int:pk>/edit/', views.coffee_update, name='coffee_update'),
    path('<int:pk>/delete/', views.coffee_delete, name='coffee_delete'),
]