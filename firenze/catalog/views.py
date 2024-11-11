from django.views.generic import TemplateView

class CatalogView(TemplateView):
    template_name = "catalog.html"

class ProductView(TemplateView):
    template_name = "product.html"