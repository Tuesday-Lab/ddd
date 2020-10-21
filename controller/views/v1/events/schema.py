from rest_framework import serializers


class SampleResponseSerializer(serializers.Serializer):
    text = serializers.CharField()


class EventResponse(serializers.Serializer):
    id = serializers.IntegerField()
