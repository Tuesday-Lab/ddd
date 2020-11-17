from rest_framework import serializers


class SignupSchema(serializers.Serializer):
    id = serializers.IntegerField()
