from django.views.generic import TemplateView
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect

from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.serializers import ValidationError
from rest_framework.parsers import FileUploadParser

from drf_spectacular.utils import OpenApiTypes, extend_schema

from personal.serializers import ChangeFavouritesSerializer, ChangePersonalSerializer, LoginSerializer, RegistrationSerializer, RequestChangePasswordSerializer, ChangePasswordSerializer
from shared.serializers import CommonResponse

from personal.models import Customer
from personal.logic import Favourites
from catalog.models import Product
from catalog.logic import GetProductFormatted
from order.models import Order

class FavouritesView(TemplateView):
    template_name = "favourites.html"

    def get(self, request):
        if not(request.user.is_authenticated):
            return redirect("/login/")
        return super().get(request)


    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        cart = Favourites(self.request)
        product_ids = cart.get_context_data()

        products = Product.objects.filter(id__in=product_ids).prefetch_related("producttype_set").distinct()
        result_products = []
        cart = Favourites(self.request)
        for product in products:
            formated_product = GetProductFormatted.get_product_json(product, None, cart.check_if_exists(product.id))
            result_products.append(formated_product.__dict__)

        context["products"] = result_products

        return context

class AccountView(TemplateView):
    template_name = "account.html"

    def get(self, request):
        if not(request.user.is_authenticated):
            return redirect("/login/")
        return super().get(request)

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["customer"] = Customer.objects.get(user=self.request.user)
        
        return context

class OrdersView(TemplateView):
    template_name = "orders.html"

    
    def get(self, request):
        if not(request.user.is_authenticated):
            return redirect("/login/")
        return super().get(request)
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["orders"] = Order.objects.filter(customer__user__id = self.request.user.id)
        
        return context
class LoginView(TemplateView):
    template_name = "login.html"
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/account/")
        return super().get(request)

class SignUpView(TemplateView):
    template_name = "sign_up.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/account/")
        return super().get(request)

class ChangePasswordRequestView(TemplateView):
    template_name = "change_password_request.html"

class ChangePasswordSubmitView(TemplateView):
    template_name = "change_password_submit.html"

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
        serializer = self.get_serializer_class()(data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            data = serializer.add_to_favourites(request, serializer.validated_data.get("product_id"))
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
        serializer = self.get_serializer_class()(data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            data = serializer.delete_from_favourites(request, serializer.validated_data.get("product_id"))
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
        user = authenticate(request, username=request.data.get("mail"), password=request.data.get("password"))
        if user is not None:
            login(request, user)
            return Response({"success": True, "redirect_link": "/account/"})
        return Response({"success": False, "message": "Данные неверныe, попробуйте ещё раз"})

class LogoutAPIView(GenericAPIView):
    
    renderer_classes = [JSONRenderer]

    def post(self, request): 
        logout(request)
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
        
        try:
            serializer = self.get_serializer_class()(data=request.data)
            
            if (serializer.is_valid(raise_exception=True)):
                user = serializer.create(serializer.validated_data)
                login(request, user)
        except IntegrityError as e:
            return Response({'success': False, "message": "Аккаунт с такой почтой уже существует"})     
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
        try:
            serializer = self.get_serializer_class()(data=request.data)
            
            if (serializer.is_valid(raise_exception=True)):
                user = serializer.update(request, serializer.validated_data)

        except ValueError as e:
            return Response({'success': False, "message": f"{str(e)}"})   

        except Exception as e:
            return Response({'success': False, "message": f"{str(e)}Произошла ошибка при сохранении данных, попробуйте позже или обратитесь в техническую поддержку"})     
        
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

class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request):
        file_obj = request.FILES['file']
        # do some stuff with uploaded file
        return Response(status=204)