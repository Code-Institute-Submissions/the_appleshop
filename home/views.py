from django.shortcuts import render, redirect

def index(request):
    """
    A view that displays an index page, in this case the overview of products
    """
    return redirect('products')