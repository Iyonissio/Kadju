import random

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

#from .forms import AddToCartForm
from .models import Category, Product

#from apps.cart.cart import Cart

def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    context = {

        'product': product,
    }

    return render(request, 'product/product.html', context)

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'category': category})
