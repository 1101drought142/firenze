from rest_framework import serializers
from django.contrib.auth.models import User
from personal.models import Customer
from personal.logic import Favourites
from django.db import transaction
from django.contrib.auth import authenticate,update_session_auth_hash 

class ChangeFavouritesSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()

    def add_to_favourites(self, request, product_id):
        cart = Favourites(request)
        cart.add(product_id)

    def delete_from_favourites(self, request, product_id):
        cart = Favourites(request)
        cart.delete(product_id)

class ChangePersonalSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    surname = serializers.CharField(required=False)
    mail = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False, format="%d.%m.%Y", input_formats=["%d.%m.%Y"])

    old_password = serializers.CharField(required=False)
    new_password = serializers.CharField(required=False)

    @transaction.atomic
    def update(self, request, validated_data):

        user = request.user
        if (validated_data["name"]):
            user.first_name = validated_data["name"]
        if (validated_data["surname"]):
            user.last_name = validated_data["surname"]
        if (validated_data["mail"]):
            user.username=validated_data["mail"]
            user.email=validated_data["mail"]
        user.save()

        customer = user.customer
        if (validated_data["phone"]):
            customer.phone_number = validated_data["phone"]
        if (validated_data["birth_date"]):
            customer.birth_date = validated_data["birth_date"]
        customer.save()

        if (validated_data.get("old_password") and validated_data.get("new_password")):
            if (len(validated_data.get("new_password")) < 6):
                raise ValueError("Новый пароль слишком простой")

            if (len(validated_data.get("new_password")) == validated_data.get("new_password")):
                raise ValueError("Новый пароль совпадает со старым")
            
            if (authenticate(request, username=user.username, password=validated_data["old_password"]) != None):
                user.set_password(validated_data.get("new_password"))
                user.save()

                update_session_auth_hash(request, user)

            else:
                raise ValueError("Старый пароль неверный")
        return True


    

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(required=False)
    mail = serializers.CharField(required=False)
    password = serializers.CharField()

class RegistrationSerializer(serializers.Serializer):
    name = serializers.CharField()
    surname = serializers.CharField()
    mail = serializers.CharField()
    phone = serializers.CharField()
    birth_date = serializers.DateField(required=False, format="%d.%m.%Y", input_formats=["%d.%m.%Y"])

    password = serializers.CharField()
    passwordConfirm = serializers.CharField()

    def validate(self, data):
        if (data["password"] != data["passwordConfirm"]):
            raise serializers.ValidationError("Пароль и подтверждение не совпадают")
        return data

    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["mail"],
            email=validated_data["mail"],
            password=validated_data["password"],
            first_name=validated_data["name"],
            last_name=validated_data["surname"],
        )
        customer = user.customer
        customer.phone_number = validated_data["phone"]
        customer.birth_date = validated_data["birth_date"]
        customer.save()
        return user
        
class RequestChangePasswordSerializer(serializers.Serializer):
    mail = serializers.CharField()

class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    secret_code = serializers.CharField()

    