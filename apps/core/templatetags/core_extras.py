from django import template

register = template.Library()

@register.filter
def in_product(products, category):
    return products.filter(category=category) 