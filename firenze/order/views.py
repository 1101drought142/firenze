from django.views.generic import TemplateView

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from drf_spectacular.utils import OpenApiTypes, extend_schema

from order.serializers import OrderSerializer
from shared.serializers import CommonResponse

class OrderView(TemplateView):
    template_name = "order.html"

class OrderThanksView(TemplateView):
    template_name = "thanks.html"


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
        #raise ValueError(self.serializer.is_valid())
        return Response({"success": True})