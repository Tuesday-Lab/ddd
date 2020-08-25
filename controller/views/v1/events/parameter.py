from rest_framework import serializers


class SampleRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
