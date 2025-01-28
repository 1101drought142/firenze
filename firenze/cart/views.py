from django.views.generic import TemplateView

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from drf_spectacular.utils import OpenApiTypes, extend_schema

from cart.serializers import ChangeCartSerializer, ChangeCartProductVariantSerializer
from shared.serializers import CommonResponse
from catalog.logic import GetProductFormatted
from catalog.models import Product, ProductType

from cart.logic import Cart

class CartView(TemplateView):
    template_name = "cart.html"

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

        return context

class AddToCartAPIView(GenericAPIView):
    
    renderer_classes = [JSONRenderer]
    serializer_class = ChangeCartSerializer

    @extend_schema(
        parameters=[ChangeCartSerializer],
        request=ChangeCartSerializer,
        responses=CommonResponse,
        description="Adding product to cart"
    )

    def post(self, request): 
        #raise ValueError(self.serializer.is_valid())

        if (request.data.get("variantId")):
            cart = Cart(request)
            cart.add(request.data.get("variantId"))
        return Response({"success": True})

class DeleteFromCartAPIView(GenericAPIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cart_wrapper.html'
    serializer_class = ChangeCartSerializer

    @extend_schema(
        parameters=[ChangeCartSerializer],
        request=ChangeCartSerializer,
        responses=CommonResponse,
        description="Delete product from cart"
    )

    def post(self, request): 
        
        
        context = {}
        cart = Cart(request)
        cart.delete(request.data.get("variant_id"))
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

        return Response(context)

        return Response({"success": True})

class ChangeCartProductVariantAPIView(GenericAPIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cart_wrapper.html'
    serializer_class = ChangeCartProductVariantSerializer

    @extend_schema(
        parameters=[ChangeCartProductVariantSerializer],
        request=ChangeCartProductVariantSerializer,
        responses=CommonResponse,
        description="Change product variant in cart"
    )

    def post(self, request): 
        context = {}
        cart = Cart(request)
        cart.delete(request.data.get("product_id"))
        cart.add(request.data.get("variant_id"))
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

        return Response(context)