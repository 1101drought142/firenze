from django.views.generic import TemplateView
import json
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from drf_spectacular.utils import OpenApiTypes, extend_schema

from catalog.serializers import SearchSerializer, FilterSerializer, ChangeProdutTypeRequest
from catalog.models import Product, ProductType
from catalog.logic import GetProductFormatted, Filter

from shared.views import PaginationView

from personal.logic import Favourites
class CatalogView(TemplateView):
    template_name = "catalog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(producttype__isnull=False).prefetch_related("producttype_set").distinct()
        result_products = []
        cart = Favourites(self.request)
        for product in products:
            
            formated_product = GetProductFormatted.get_product_json(product, None, cart.check_if_exists(product.id))
            result_products.append(formated_product.__dict__)

        context["filter"] = Filter.get_filter_context(products)



        paginator = PaginationView(9, list(result_products), 1)
        products = paginator.current_page.object_list
        pagination = paginator.get_pagintaion_context()

        context["products"] = products
        context["pagination"] = pagination
       
        return context

class ProductView(TemplateView):
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(id=kwargs.get("id"))
        cart = Favourites(self.request)
        formated_product = GetProductFormatted.get_product_json(product, None, cart.check_if_exists(product.id))
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
        cart = Favourites(self.request)
        for product in queryset:
            formated_product = GetProductFormatted.get_product_json(product, None, cart.check_if_exists(product.id))
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


        filter_values = {}

        if (request.query_params.get("sizes")):
            filter_values["producttype__size_id__in"] = request.query_params.getlist("sizes")

        if (request.query_params.get("mat")):
            filter_values["producttype__material_id__in"] = request.query_params.getlist("mat")

        if (request.query_params.get("color")):
            filter_values["producttype__color_id__in"] = request.query_params.getlist("color")


        if (request.query_params.get("priceMin")):
            filter_values["producttype__price__gte"] = request.query_params.get("priceMin")
        
        if (request.query_params.get("priceMax")):
            filter_values["producttype__price__lte"] = request.query_params.get("priceMax")

        order_by = "name"
        if (request.query_params.get("sort")):
            if request.query_params.get("sort") == "byPopular":
                order_by = "name"
            if request.query_params.get("sort") == "byPriceLow":
                order_by = "price"
            if request.query_params.get("sort") == "byPriceHigh":
                order_by = "-price"



        products = Product.objects.filter(**filter_values).prefetch_related("producttype_set").order_by(order_by).distinct()

        #raise ValueError([filter_values,products])
        result_products = []
        cart = Favourites(request)
        for product in products:
            formated_product = GetProductFormatted.get_product_json(product, None, cart.check_if_exists(product.id))
            result_products.append(formated_product.__dict__)

        page_num = request.query_params.get("page")
        paginator = PaginationView(9, list(result_products), page_num)
        products = paginator.current_page.object_list
        pagination = paginator.get_pagintaion_context()

        return Response({
            "products": products,
            'pagination': pagination
        })

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
        cart = Favourites(self.request)
        product = Product.objects.get(id=request.query_params.get("product_id"))
        variant = ProductType.objects.get(id=request.query_params.get("variant_id"))
        formated_product = GetProductFormatted.get_product_json(product, variant, cart.check_if_exists(product.id))
        return Response({"product": formated_product.__dict__})


