from django.urls import path

from personal.views import (
    FavouritesView,
    AccountView,
    OrdersView,
    LoginView,
    SignUpView
)

urlpatterns = [
    path('favourites/', FavouritesView.as_view(), name='favourites_page'),
    path('account/', AccountView.as_view(), name='account_page'),
    path('orders/', OrdersView.as_view(), name='orders_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('sign_up/', SignUpView.as_view(), name='signup_page'),
]