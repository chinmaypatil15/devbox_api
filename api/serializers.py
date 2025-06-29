from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class APIUsageSerializer(serializers.Serializer):
    endpoint = serializers.CharField()
    method = serializers.ChoiceField(choices=["GET", "POST", "PUT", "DELETE"])
    timestamp = serializers.DateTimeField()
