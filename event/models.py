from typing import Optional

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from base.db.mixin import TimestampMixin
from event.vo import Money, Schedule


class EventManager(models.Manager):
    def create_new(self,
                   title: str,
                   slug: str,
                   kind: str,
                   money: Money,
                   max_attendee_count: Optional[int],
                   description: str,
                   user: User,
                   schedule: Schedule,
                   ):
        return super(EventManager, self).create(
            title=title,
            slug=slug,
            kind=kind,
            host_user=user,
            amount=money.amount,
            currency=money.currency,
            max_attendee_count=max_attendee_count,
            description=description,
            start_time=schedule.start_time,
            end_time=schedule.end_time,
        )


class Event(TimestampMixin, models.Model):
    class EventKind(models.TextChoices):
        NORMAL = "NORMAL"
        EDU = "EDU"
        PROMOTION = "PROMOTION"

    id = models.BigAutoField(primary_key=True)
    host_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    max_attendee_count = models.IntegerField(null=True)
    # geo_location = gis_models.PointField(null=True, blank=True)   # TODO 필요할 때 작업
    main_image = models.FilePathField()
    description = models.TextField()
    registrable_time = models.DateTimeField(null=True)
    is_visible = models.BooleanField(default=False)
    objects = EventManager()

    class Meta:
        db_table = 'event'

    @property
    def is_unlimited(self):
        return self.max_attendee_count is None
