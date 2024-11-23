from django.views.generic import TemplateView

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from drf_spectacular.utils import OpenApiTypes, extend_schema

from personal.serializers import ChangeFavouritesSerializer, ChangePersonalSerializer, LoginSerializer, RegistrationSerializer, RequestChangePasswordSerializer, ChangePasswordSerializer
from shared.serializers import CommonResponse

class FavouritesView(TemplateView):
    template_name = "favourites.html"

class AccountView(TemplateView):
    template_name = "account.html"

class OrdersView(TemplateView):
    template_name = "orders.html"
    
class LoginView(TemplateView):
    template_name = "login.html"

class SignUpView(TemplateView):
    template_name = "sign_up.html"

class AddToFavouritesAPIView(GenericAPIView):
    
    renderer_classes = [JSONRenderer]
    serializer_class = ChangeFavouritesSerializer

    @extend_schema(
        parameters=[ChangeFavouritesSerializer],
        request=ChangeFavouritesSerializer,
        responses=CommonResponse,
        description="Adding product to favourites"
    )

    def post(self, request): 
        #raise ValueError(self.serializer.is_valid())
        return Response({"success": True})

class DeleteFromFavouritesAPIView(GenericAPIView):
    
    renderer_classes = [JSONRenderer]
    serializer_class = ChangeFavouritesSerializer

    @extend_schema(
        parameters=[ChangeFavouritesSerializer],
        request=ChangeFavouritesSerializer,
        responses=CommonResponse,
        description="Delete product from favourites"
    )

    def post(self, request): 
        #raise ValueError(self.serializer.is_valid())
        return Response({"success": True})

class ChangePersonalInfoAPIView(GenericAPIView):
    
    renderer_classes = [JSONRenderer]
    serializer_class = ChangePersonalSerializer

    @extend_schema(
        parameters=[ChangePersonalSerializer],
        request=ChangePersonalSerializer,
        responses=CommonResponse,
        description="Change user personal information"
    )

    def post(self, request): 
        #raise ValueError(self.serializer.is_valid())
        return Response({"success": True})

class LoginAPIView(GenericAPIView):
    
    renderer_classes = [JSONRenderer]
    serializer_class = LoginSerializer

    @extend_schema(
        parameters=[LoginSerializer],
        request=LoginSerializer,
        responses=CommonResponse,
        description="User login"
    )

    def post(self, request): 
        #raise ValueError(self.serializer.is_valid())
        return Response({"success": True})

class LogoutAPIView(GenericAPIView):
    
    renderer_classes = [JSONRenderer]

    def post(self, request): 
        #raise ValueError(self.serializer.is_valid())
        return Response({"success": True})

class RegistrationAPIView(GenericAPIView):
    
    renderer_classes = [JSONRenderer]
    serializer_class = RegistrationSerializer

    @extend_schema(
        parameters=[RegistrationSerializer],
        request=RegistrationSerializer,
        responses=CommonResponse,
        description="User registration"
    )

    def post(self, request): 
        #raise ValueError(self.serializer.is_valid())
        return Response({"success": True})

class RequestChangePasswordAPIView(GenericAPIView):
    
    renderer_classes = [JSONRenderer]
    serializer_class = RequestChangePasswordSerializer

    @extend_schema(
        parameters=[RequestChangePasswordSerializer],
        request=RequestChangePasswordSerializer,
        responses=CommonResponse,
        description="Request password change"
    )

    def post(self, request): 
        #raise ValueError(self.serializer.is_valid())
        return Response({"success": True})

class ChangePasswordAPIView(GenericAPIView):
    
    renderer_classes = [JSONRenderer]
    serializer_class = ChangePasswordSerializer

    @extend_schema(
        parameters=[ChangePasswordSerializer],
        request=ChangePasswordSerializer,
        responses=CommonResponse,
        description="Change password"
    )

    def post(self, request): 
        #raise ValueError(self.serializer.is_valid())
        return Response({"success": True})