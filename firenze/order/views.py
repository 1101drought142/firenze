from django.views.generic import TemplateView

class OrderView(TemplateView):
    template_name = "order.html"

class OrderThanksView(TemplateView):
    template_name = "thanks.html"
