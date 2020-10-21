from django.db import models
from pydantic import BaseModel, validator

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


class Event(TimestampMixin, models.Model):
    # class EventKind(models.TextChoices):
    #     pass

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    # host_user_id = models.ForeignKey(User) # TODO Custom Event User
    slug = models.SlugField(unique=True)

    kind = models.CharField(max_length=10)  # Todo EventKind
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    currency = models.CharField(max_length=3)
    max_attendee_count = models.IntegerField()
    # geo_location = gis_model.PointField()
    main_image = models.FilePathField()
    description = models.TextField()
    registrable_time = models.DateTimeField(null=True)
    is_visible = models.BooleanField(default=False)

    class Meta:
        db_table = 'event'
