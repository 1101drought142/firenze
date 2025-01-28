from django.views.generic import TemplateView
from django.shortcuts import redirect

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from drf_spectacular.utils import OpenApiTypes, extend_schema

from order.serializers import OrderSerializer
from shared.serializers import CommonResponse
from catalog.logic import GetProductFormatted
from catalog.models import Product, ProductType

from cart.logic import Cart
from main.models import Shops
from personal.models import Customer
from order.models import Order

class OrderView(TemplateView):
    template_name = "order.html"

    def get(self, request):
        cart = Cart(request)
        cart_data = cart.get_context_data()
        variants = cart_data.keys()
        if (not(variants)):
            return redirect("/catalog/")
        return super().get(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        cart_data = cart.get_context_data()

        variants = cart_data.keys()

        

        summ_price = 0

        product_types = ProductType.objects.filter(id__in=variants)
        result_products = {

        }


        for product_type in product_types:
            summ_price += product_type.price
            product = Product.objects.get(id=product_type.product.id)
            formated_product = GetProductFormatted.get_product_json(product, product_type)
            
            result_products[product_type.id] = {
                "product": formated_product.__dict__,
                "count": cart_data[str(product_type.id)]
            }
            
    
        context["cart_items"] = result_products
        context["price"] = summ_price

        shops = Shops.objects.all()
        result = {

        }
        for shop in shops:
            if not(result.get(shop.shop_type)):
                result[shop.shop_type] = [shop]
            else:
                result[shop.shop_type].append(shop)

        context["shops"] = result
        if (self.request.user.id):
            context["user"] = self.request.user
            context["customer"] = Customer.objects.get(user=self.request.user)
        return context

class OrderThanksView(TemplateView):
    template_name = "thanks.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["id"] = kwargs["id"]
        return context

class OrderAPIView(GenericAPIView):
    
    renderer_classes = [JSONRenderer]
    serializer_class = OrderSerializer

    @extend_schema(
        parameters=[OrderSerializer],
        request=OrderSerializer,
        responses=CommonResponse,
        description="Complete Order"
    )

    def post(self, request): 
        cart = Cart(self.request)
        cart_data = cart.get_context_data()
        variants = cart_data.keys()
        summ_price = 0
        product_types = ProductType.objects.filter(id__in=variants)
        for product_type in product_types:
            summ_price += product_type.price

        shop = Order()
        shop.name = request.data.get("name")
        shop.last_name = request.data.get("surname")
        shop.phone_number = request.data.get("code")
        shop.mail = request.data.get("mail")
        shop.shop = Shops.objects.get(id=request.data.get("shop"))
        shop.price = summ_price
        if (request.user.id):
            shop.customer = Customer.objects.get(user=request.user)
        shop.save()

        
        

        for variant in variants:
            shop.cart_items.add(ProductType.objects.get(id=variant))

        #raise ValueError(self.serializer.is_valid())
        return Response({"success": True, "redirect_link": f"/thanks/{shop.id}/"})