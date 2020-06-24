from django.shortcuts import render, get_object_or_404
from .models import Product
from checkout.models import OrderLineItem

def all_products(request):
    products = Product.objects.all()
    purchased_products=[]
    if request.user.is_authenticated:
        orderline_items= OrderLineItem.objects.filter(user=request.user)
        if orderline_items:
            for lineitem in orderline_items:
                purchased_products.append(lineitem.product.name)
    return render(request, 'products.html', {'products': products, 'purchased_products': purchased_products})

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    product.view_count += 1
    product.save()
    purchased_products=[]
    if request.user.is_authenticated:
        orderline_items= OrderLineItem.objects.filter(user=request.user)
        if orderline_items:
            for lineitem in orderline_items:
                purchased_products.append(lineitem.product.name)
    return render(request, "productdetail.html", {'product': product, 'purchased_products': purchased_products})