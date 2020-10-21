from rest_framework import serializers

from base.serializers import EnumField
from event.models import Currency


class SampleRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)


class CreateEventParameters(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    slug = serializers.SlugField()
    kind = serializers.CharField(max_length=10)
    amount = serializers.DecimalField(max_digits=11, decimal_places=2)
    currency = EnumField(choices=Currency)
    # currency = serializers.ChoiceField(choices=Currency.values())

    max_attendee_count = serializers.IntegerField()
    description = serializers.CharField(max_length=1000)
