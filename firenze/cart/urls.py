from django.urls import path

from cart.views import (
    CartView,
)

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart_page'),
]