from rest_framework import serializers

class SearchSerializer(serializers.Serializer):
    query = serializers.CharField(max_length=255, min_length=3)

class FilterSerializer(serializers.Serializer):
    category = serializers.IntegerField()
    size = serializers.IntegerField()
    material = serializers.IntegerField()
    color = serializers.IntegerField()
    min_price = serializers.IntegerField()
    max_price = serializers.IntegerField()
    current_page = serializers.IntegerField()
    order_by = serializers.CharField(required=False)
    order = serializers.CharField(required=False)

class ChangeProdutTypeRequest(serializers.Serializer):
    variant_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
  