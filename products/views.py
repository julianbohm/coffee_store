from django.shortcuts import render
from .models import Coffee

# Create your views here.

def coffee_list(request):
    coffees = Coffee.objects.filter(available=True)
    return render(request, 'products/coffee_list.html', {'coffees': coffees})