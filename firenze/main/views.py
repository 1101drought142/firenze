from django.views.generic import TemplateView
from catalog.models import (
    Product,
    Collections
)
from main.models import Shops, News
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        show_on_main_page = Product.objects.filter(show_on_main_page=True, big_image=False)[:4]
        big_picture = Product.objects.filter(show_on_main_page=True, big_image=True).first()
        collections = Collections.objects.all()[:2]

        context["show_on_main"] = show_on_main_page
        context["big_picture"] = big_picture
        context["collections"] = collections

        return context

class AboutView(TemplateView):
    template_name = "about.html"

class ShopsView(TemplateView):
    template_name = "shops.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        shops = Shops.objects.all()
        result = {

        }
        for shop in shops:
            if not(result.get(shop.shop_type)):
                result[shop.shop_type] = [shop]
            else:
                result[shop.shop_type].append(shop)

        context["shops"] = result
        return context

class NewsView(TemplateView):
    template_name = "news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = News.objects.all()
        context["news"] = news
        return context

class NewsItemView(TemplateView):
    template_name = "news_item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = News.objects.get(slug=kwargs["slug"])
        context["news"] = news
        return context

class ReturnRulesView(TemplateView):
    template_name = "info_page.html"

class PaymentView(TemplateView):
    template_name = "info_page.html"

class ShippingView(TemplateView):
    template_name = "info_page.html"