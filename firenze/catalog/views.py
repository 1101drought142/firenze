from django.views.generic import TemplateView

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from drf_spectacular.utils import OpenApiTypes, extend_schema

from catalog.serializers import SearchSerializer, FilterSerializer, ChangeProdutTypeRequest


class CatalogView(TemplateView):
    template_name = "catalog.html"

class ProductView(TemplateView):
    template_name = "product.html"

class SearchAPIView(GenericAPIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'test_search.html'
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
        #raise ValueError(self.serializer.is_valid())
        return Response()


class FilterAPIView(GenericAPIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'test_search.html'
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
        #raise ValueError(self.serializer.is_valid())
        return Response()

class ChangeProductParamAPIView(GenericAPIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'test_change.html'
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
        #raise ValueError(self.serializer.is_valid())
        return Response()


