from django.urls import path
from import_1c.views import ImportCatalogView

urlpatterns = [
    path('import/catalog', ImportCatalogView.as_view(), name='import_catalog'),
]