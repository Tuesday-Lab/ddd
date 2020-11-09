from rest_framework import serializers


class EventResponse(serializers.Serializer):
    id = serializers.IntegerField()
