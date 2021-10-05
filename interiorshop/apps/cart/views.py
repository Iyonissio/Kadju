from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from .cart import Cart

def cart_detail(request):
    return render(request, 'cart/cart.html')

def success(request):
    return render(request, 'cart/success.html')
