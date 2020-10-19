from django.db import models

from base.db.mixin import TimestampMixin


class Event(TimestampMixin, models.Model):
    # class EventKind(models.TextChoices):
    #     pass

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    # host_user_id = models.ForeignKey(User) # TODO Custom Event User
    slug = models.SlugField()

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
