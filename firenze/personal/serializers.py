from rest_framework import serializers

class ChangeFavouritesSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()

class ChangePersonalSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    surname = serializers.CharField(required=False)
    mail = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)

    old_password = serializers.CharField(required=False)
    new_password = serializers.CharField(required=False)

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(required=False)
    mail = serializers.CharField(required=False)
    password = serializers.CharField()

class RegistrationSerializer(serializers.Serializer):
    name = serializers.CharField()
    surname = serializers.CharField()
    mail = serializers.CharField()
    phone = serializers.CharField()
    birth_date = serializers.DateField(required=False)

    password = serializers.CharField()
    confirm_password = serializers.CharField()

class RequestChangePasswordSerializer(serializers.Serializer):
    mail = serializers.CharField()

class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    secret_code = serializers.CharField()