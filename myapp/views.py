from django.shortcuts import render
from .models import Product

def index(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    
    # Pass the products to the template for rendering
    return render(request, 'index.html', {'products': products})

def show(request, pk):
    # Retrieve the product with the given primary key (pk) from the database
    product = Product.objects.get(pk=pk)
    
    # Pass the product to the template for rendering
    return render(request, 'show.html', {'product': product})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

