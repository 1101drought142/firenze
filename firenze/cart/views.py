from django.views.generic import TemplateView

class CartView(TemplateView):
    template_name = "cart.html"