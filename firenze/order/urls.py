from django.urls import path

from order.views import (
    OrderView,
    OrderThanksView,
    OrderAPIView
)

urlpatterns = [
    path('order/', OrderView.as_view(), name='order_page'),
    path('thanks/', OrderThanksView.as_view(), name='thanks_page'),

    path('api/v1/order/order', OrderAPIView.as_view(), name="order_api"),

]