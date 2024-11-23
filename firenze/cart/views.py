from django.views.generic import TemplateView

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from drf_spectacular.utils import OpenApiTypes, extend_schema

from cart.serializers import ChangeCartSerializer, ChangeCartProductVariantSerializer
from shared.serializers import CommonResponse

class CartView(TemplateView):
    template_name = "cart.html"

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
        return Response({"success": True})

class DeleteFromCartAPIView(GenericAPIView):
    
    renderer_classes = [JSONRenderer]
    serializer_class = ChangeCartSerializer

    @extend_schema(
        parameters=[ChangeCartSerializer],
        request=ChangeCartSerializer,
        responses=CommonResponse,
        description="Delete product from cart"
    )

    def post(self, request): 
        #raise ValueError(self.serializer.is_valid())
        return Response({"success": True})

class ChangeCartProductVariantAPIView(GenericAPIView):
    
    renderer_classes = [JSONRenderer]
    serializer_class = ChangeCartProductVariantSerializer

    @extend_schema(
        parameters=[ChangeCartProductVariantSerializer],
        request=ChangeCartProductVariantSerializer,
        responses=CommonResponse,
        description="Change product variant in cart"
    )

    def post(self, request): 
        #raise ValueError(self.serializer.is_valid())
        return Response({"success": True})