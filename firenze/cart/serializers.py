from rest_framework import serializers

class ChangeCartSerializer(serializers.Serializer):
    variant_id = serializers.IntegerField()

class ChangeCartProductVariantSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    variant_id = serializers.IntegerField()