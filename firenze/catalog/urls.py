from django.urls import path

from catalog.views import (
    CatalogView,
    ProductView
)

urlpatterns = [
    path('catalog/', CatalogView.as_view(), name='catalog_page'),
    path('product/', ProductView.as_view(), name='product_page'),
]