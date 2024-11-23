from django.urls import path

from cart.views import (
    CartView,
    AddToCartAPIView,
    DeleteFromCartAPIView,
    ChangeCartProductVariantAPIView
)

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart_page'),

    path('api/v1/cart/add_to_cart', AddToCartAPIView.as_view(), name="add_to_cart_api"),
    path('api/v1/cart/delete_from_cart', DeleteFromCartAPIView.as_view(), name="delete_from_cart_api"),
    path('api/v1/cart/change_cart_prodct_variant', ChangeCartProductVariantAPIView.as_view(), name="delete_from_cart_api"),
]