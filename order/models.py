from django.db import models

from base import settings
from base.db.mixin import TimestampMixin


class OrderModel(TimestampMixin):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey("event.EventModel", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    pay_method = models.CharField(max_length=10)
    paid_amount = models.FloatField()
    paid_at = models.DateTimeField(null=True)
    canceled_at = models.DateTimeField(null=True)
    refunded_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "order"
