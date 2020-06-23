from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    product.view_count += 1
    product.save()
    return render(request, "productdetail.html", {'product': product})