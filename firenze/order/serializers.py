from rest_framework import serializers

class OrderSerializer(serializers.Serializer):
    
    name = serializers.CharField(required=False)
    surname = serializers.CharField(required=False)
    mail = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)

    city = serializers.CharField(required=False)
    street = serializers.CharField(required=False)
    index = serializers.CharField(required=False)

    payment_id = serializers.IntegerField(required=False)
    shop_id = serializers.IntegerField(required=False)