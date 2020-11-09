from base.serializers import EnumField
from rest_framework import serializers

from event.models import Event
from event.vo import Currency


class CreateEventParameters(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    slug = serializers.SlugField()
    kind = serializers.ChoiceField(choices=Event.EventKind.names)
    amount = serializers.DecimalField(max_digits=11, decimal_places=2)
    currency = EnumField(choices=Currency)

    max_attendee_count = serializers.IntegerField(allow_null=True)
    description = serializers.CharField(max_length=1000)
    start_time = serializers.DateTimeField(allow_null=True, required=False)
    end_time = serializers.DateTimeField(allow_null=True, required=False)

    def validate_max_attendee_count(self, value):
        """
        Check that the blog post is about Django.
        """
        if not value and value <= 0:
            raise ValueError("max attendee count should be grater than 0")
        return value
