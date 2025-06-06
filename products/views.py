from django.shortcuts import render, get_object_or_404, redirect
from .models import Coffee
from .forms import CoffeeForm

def coffee_list(request):
    coffees = Coffee.objects.filter(available=True)
    return render(request, 'products/coffee_list.html', {'coffees': coffees})

def coffee_detail(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    return render(request, 'products/coffee_detail.html', {'coffee': coffee})

def coffee_create(request):
    if request.method == 'POST':
        form = CoffeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('coffee_list')
    else:
        form = CoffeeForm()
    return render(request, 'products/coffee_form.html', {'form': form})

def coffee_update(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    if request.method == 'POST':
        form = CoffeeForm(request.POST, request.FILES, instance=coffee)
        if form.is_valid():
            form.save()
            return redirect('coffee_list')
    else:
        form = CoffeeForm(instance=coffee)
    return render(request, 'products/coffee_form.html', {'form': form})

def coffee_delete(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    if request.method == 'POST':
        coffee.delete()
        return redirect('coffee_list')
    return render(request, 'products/coffee_confirm_delete.html', {'coffee': coffee})