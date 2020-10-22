from django.db import models
# from django.contrib.gis.db import models as gis_models
from pydantic import BaseModel, validator

from base import settings
from base.db.mixin import TimestampMixin
from base.extension import ExtendedEnum


class Currency(str, ExtendedEnum):
    KRW = "KRW"
    USD = "USD"


class Money(BaseModel):
    amount: int
    currency: Currency

    @validator('amount')
    def amount_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("amount should be grater then 0")
        return v


class EventManager(models.Manager):
    def create_new(self,
                   title: str,
                   slug: str,
                   kind: str,
                   money: Money,
                   max_attendee_count: str,
                   description: str
                   ):
        return super(EventManager, self).create(
            title=title,
            slug=slug,
            kind=kind,
            amount=money.amount,
            currency=money.currency,
            max_attendee_count=max_attendee_count,
            description=description
        )


class Event(TimestampMixin, models.Model):
    class EventKind(models.TextChoices):
        NORMAL = "NORMAL"
        EDU = "EDU"
        PROMOTION = "PROMOTION"

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
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
    # geo_location = gis_models.PointField(null=True, blank=True)   # TODO 필요할 때 작업
    main_image = models.FilePathField()
    description = models.TextField()
    registrable_time = models.DateTimeField(null=True)
    is_visible = models.BooleanField(default=False)
    objects = EventManager()

    class Meta:
        db_table = 'event'
