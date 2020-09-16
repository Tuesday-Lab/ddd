from django.db import models
from django.contrib.gis.db import models as gis_model

from ddd.event.infrastructure.models.base import TimestampMixin
from ddd.event.infrastructure.models.user import User


class Event(TimestampMixin):
    class EventKind(models.TextChoices):
        pass

    id = models.BigAutoField()
    title = models.CharField(max_length=255)
    host_user_id = models.ForeignKey(User)
    slug = models.SlugField()

    kind = models.CharField(choices=EventKind.choices)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    amount = models.DecimalField(decimal_places=2)
    currency = models.CharField()
    max_attendee_count = models.IntegerField()
    geo_location = gis_model.PointField()
    main_image = models.FilePathField()
    description = models.TextField()
    registrable_time = models.DateTimeField(null=True)
    is_visible = models.BooleanField(default=False)
