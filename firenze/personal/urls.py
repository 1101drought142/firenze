from django.urls import path

from personal.views import (
    FavouritesView,
    AccountView,
    OrdersView,
    LoginView,
    SignUpView,

    AddToFavouritesAPIView,
    DeleteFromFavouritesAPIView,
    ChangePersonalInfoAPIView,
    LoginAPIView,
    LogoutAPIView,
    RegistrationAPIView,
    RequestChangePasswordAPIView,
    ChangePasswordAPIView
)

urlpatterns = [
    path('favourites/', FavouritesView.as_view(), name='favourites_page'),
    path('account/', AccountView.as_view(), name='account_page'),
    path('orders/', OrdersView.as_view(), name='orders_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('sign_up/', SignUpView.as_view(), name='signup_page'),

    path('api/v1/personal/add_to_favourites', AddToFavouritesAPIView.as_view(), name="add_to_favourites_api"),
    path('api/v1/personal/delete_from_favourites', DeleteFromFavouritesAPIView.as_view(), name="delete_from_favourites_api"),
    path('api/v1/personal/change_info', ChangePersonalInfoAPIView.as_view(), name="change_info_api"),
    path('api/v1/personal/login', LoginAPIView.as_view(), name="login_api"),
    path('api/v1/personal/logout', LogoutAPIView.as_view(), name="logout_api"),
    path('api/v1/personal/registration', RegistrationAPIView.as_view(), name="registration_api"),
    path('api/v1/personal/request_password_change', RequestChangePasswordAPIView.as_view(), name="request_password_change_api"),
    path('api/v1/personal/change_password', ChangePasswordAPIView.as_view(), name="change_password_api"),
]