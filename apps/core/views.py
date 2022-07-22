from django.shortcuts import render, get_object_or_404
from apps.cart.forms import CartAddProductForm
from .models import Category, Product, Type

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    types = Type.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories,
                'products': products, 'types': types}
    return render(request, 'core/index.html', context)


# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     context = {'product': product, 'cart_product_form': cart_product_form}
#     return render(request, 'core/product/detail.html', context)
