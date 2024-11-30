from django.views.generic import TemplateView
import json
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from drf_spectacular.utils import OpenApiTypes, extend_schema

from catalog.serializers import SearchSerializer, FilterSerializer, ChangeProdutTypeRequest
from catalog.models import Product, ProductType

from catalog.logic import GetProductFormatted

class CatalogView(TemplateView):
    template_name = "catalog.html"

class ProductView(TemplateView):
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(id=1)
        formated_product = GetProductFormatted.get_product_json(product)
        context["product"] = formated_product.__dict__

        return context

class SearchAPIView(GenericAPIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'search.html'
    serializer_class = SearchSerializer

    @extend_schema(
        parameters=[SearchSerializer],
        request=SearchSerializer,
        responses={
            200: OpenApiTypes.STR,
            #400: OpenApiTypes.OBJECT,  
        },
        description="Product search"
    )

    def get(self, request): 
        queryset = Product.objects.filter(name__contains=request.query_params.get("query")).prefetch_related("producttype_set")
        result_products = []
        for product in queryset:
            formated_product = GetProductFormatted.get_product_json(product)
            result_products.append(formated_product.__dict__)
            #raise ValueError(formated_product.__dict__)
        return Response({"products": result_products})


class FilterAPIView(GenericAPIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'filter.html'
    serializer_class = FilterSerializer

    @extend_schema(
        parameters=[FilterSerializer],
        request=FilterSerializer,
        responses={
            200: OpenApiTypes.STR,
            #400: OpenApiTypes.OBJECT,  
        },
        description="Catalog filtering and sorting"
    )

    def get(self, request): 
        queryset = Product.objects.filter(name__contains=request.query_params.get("query")).prefetch_related("producttype_set")
        result_products = []
        for product in queryset:
            formated_product = GetProductFormatted.get_product_json(product)
            result_products.append(formated_product.__dict__)
            #raise ValueError(formated_product.__dict__)
        return Response({"products": result_products})

class ChangeProductParamAPIView(GenericAPIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product_content.html'
    serializer_class = ChangeProdutTypeRequest

    @extend_schema(
        parameters=[ChangeProdutTypeRequest],
        request=ChangeProdutTypeRequest,
        responses={
            200: OpenApiTypes.STR,
            #400: OpenApiTypes.OBJECT,  
        },
        description="Change card from variant id"
    )

    def get(self, request): 
        product = Product.objects.get(id=request.query_params.get("product_id"))
        variant = ProductType.objects.get(id=request.query_params.get("variant_id"))
        formated_product = GetProductFormatted.get_product_json(product, variant)
        return Response({"product": formated_product.__dict__})


