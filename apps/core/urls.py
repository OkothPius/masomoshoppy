from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('books/', views.book, name='books_list'),
    path('uniforms/', views.uniform, name='uniforms_list'),
    path('stationary/', views.stationary, name='stationary_list'),
    path('electronic/', views.electronic, name='electronic_list'),
    path('equipment/', views.equipment, name='equipment_list'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),




    # path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
