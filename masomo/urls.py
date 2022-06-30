"""config URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls', namespace='core')),
    path('cart/', include('apps.cart.urls', namespace='cart')),
    path('order/', include('apps.order.urls', namespace='order')),
    path('coupon/', include('apps.coupon.urls', namespace='coupon')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
