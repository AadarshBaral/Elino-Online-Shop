import imp
from logging import exception
from django.shortcuts import render, get_object_or_404


from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page


CACHE_TTL  = getattr(settings , "CACHE_TTL",DEFAULT_TIMEOUT)

def product_list(request, category_slug=None):
    category = None

    categories = Category.objects.all()
        
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):

    try:
        if cache.get(id):
            product = cache.get(id)
          

        else:
            product = get_object_or_404(Product,
                                        id=id,
                                        slug=slug,
                                        available=True)
            cache.set(
                id , product
            )
        
        
    except exception as e:
        print(e)
        
    cart_product_form = CartAddProductForm()
    return render(request,
    'shop/product/detail.html',
    {'product': product,
    'cart_product_form': cart_product_form})
    
    
