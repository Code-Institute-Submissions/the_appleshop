from django.shortcuts import render, redirect

def index(request):
    """
    A view that displays an index page
    """
    return redirect('products')