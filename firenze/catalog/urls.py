from django.urls import path

from catalog.views import (
    CatalogView,
    ProductView,
    SearchAPIView,
    FilterAPIView,
    ChangeProductParamAPIView
)

urlpatterns = [
    path('catalog/', CatalogView.as_view(), name='catalog_page'),
    path('product/<int:id>/', ProductView.as_view(), name='product_page'),

    path('api/v1/catalog/search', SearchAPIView.as_view(), name="search_api"),
    path('api/v1/catalog/filter', FilterAPIView.as_view(), name="filter_api"),
    path('api/v1/catalog/change_product_param', ChangeProductParamAPIView.as_view(), name="change_product_param_api"),
]