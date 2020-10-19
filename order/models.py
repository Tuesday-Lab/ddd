from django.db import models

from base.db.mixin import TimestampMixin


class Order(TimestampMixin):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey("event.Event", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)  # TODO custom User
    status = models.CharField(max_length=10)
    pay_method = models.CharField(max_length=10)
    paid_amount = models.FloatField()
    paid_at = models.DateTimeField(null=True)
    canceled_at = models.DateTimeField(null=True)
    refunded_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'order'
