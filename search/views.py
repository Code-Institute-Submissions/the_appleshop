from django.shortcuts import render
from products.models import Product

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET.get('q'))
    return render(request, 'products.html', {'products': products})

def do_ext_search(request):
    searchterm=request.GET.get('q', "")
    products = Product.objects.filter(name__icontains=searchterm)
    return render(request, 'search.html', {'products': products, 'searchterm': 'searchterm'})





