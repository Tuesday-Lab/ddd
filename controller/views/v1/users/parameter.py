from rest_framework import serializers


class SignupParameters(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=30)


class SigninParameters(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
