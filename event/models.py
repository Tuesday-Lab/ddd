from django.db import models
from django.contrib.gis.db import models as gis_models

from base import settings
from base.db.mixin import TimestampMixin


class Event(TimestampMixin, models.Model):
    class EventKind(models.TextChoices):
        NORMAL = "NORMAL"
        EDU = "EDU"
        PROMOTION = "PROMOTION"

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    kind = models.CharField(
        max_length=10,
        choices=EventKind.choices,
        default=EventKind.NORMAL,
    )
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    currency = models.CharField(max_length=3)
    max_attendee_count = models.IntegerField()
    geo_location = gis_models.PointField(null=True, blank=True)
    main_image = models.FilePathField()
    description = models.TextField()
    registrable_time = models.DateTimeField(null=True)
    is_visible = models.BooleanField(default=False)

    class Meta:
        db_table = 'event'
