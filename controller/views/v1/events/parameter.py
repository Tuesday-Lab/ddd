from rest_framework import serializers

from base.serializers import EnumField
from event.vo import Currency


class CreateEventParameters(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    slug = serializers.SlugField()
    kind = serializers.CharField(max_length=10)
    amount = serializers.DecimalField(max_digits=11, decimal_places=2)
    currency = EnumField(choices=Currency)

    max_attendee_count = serializers.IntegerField(min_value=0)
    description = serializers.CharField(max_length=1000)
