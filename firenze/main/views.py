from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ShopsView(TemplateView):
    template_name = "shops.html"

class NewsView(TemplateView):
    template_name = "news.html"

class NewsItemView(TemplateView):
    template_name = "news_item.html"

class ReturnRulesView(TemplateView):
    template_name = "news_item.html"

class PaymentView(TemplateView):
    template_name = "news_item.html"

class ShippingView(TemplateView):
    template_name = "news_item.html"