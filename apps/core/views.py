from django.shortcuts import render, get_object_or_404
from apps.cart.forms import CartAddProductForm
from .models import Category, Product, Type

# Products
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


def book(request):
    products = Product.objects.all()
    types = Type.objects.all()
    context = {'products':products, 'types':types}
    return render(request, 'core/books.html', context)


#Uniforms
def uniform(request):
    products = Product.objects.filter(available=True)
    types = Type.objects.all()
    context = {'products': products, 'types': types}
    return render(request, 'core/uniforms.html', context)

# Stationary
def stationary(request, category_slug=None):
    products = Product.objects.all()
    types = Type.objects.all()
    context = {'products':products, 'types':types}
    return render(request, 'core/stationary.html', context)

# Electronics
def electronic(request, category_slug=None):
    products = Product.objects.all()
    types = Type.objects.all()
    context = {'products':products, 'types':types}
    return render(request, 'core/electronics.html', context)


# Equipments
def equipment(request, category_slug=None):
    products = Product.objects.all()
    types = Type.objects.all()
    context = {'products':products, 'types':types}
    return render(request, 'core/equipment.html', context)


def product_detail(request, id, slug):
    products = Product.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'products':products,'cart_product_form': cart_product_form}
    return render(request, 'core/product_detail.html', context)

