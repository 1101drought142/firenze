from django.urls import path

from main.views import (
    HomeView,
    AboutView,
    ShopsView,
    NewsView,
    NewsItemView,
    ReturnRulesView,
    PaymentView,
    ShippingView,

)

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('shops/', ShopsView.as_view(), name='shops_page'),
    path('news/', NewsView.as_view(), name='news_page'),
    path('news/<str:slug>/', NewsItemView.as_view(), name='news_item_page'),
    path('return/', ReturnRulesView.as_view(), name='return_page'),
    path('payment/', PaymentView.as_view(), name='payment_page'),
    path('shipping/', ShippingView.as_view(), name='shipping_page'),


]