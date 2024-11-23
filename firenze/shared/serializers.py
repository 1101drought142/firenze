from rest_framework import serializers

class CommonResponse(serializers.Serializer):
    success = serializers.BooleanField()
    message = serializers.CharField()
    redirect_link = serializers.CharField()