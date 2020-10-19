from django.db import models


class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class UpdatedAtMixin(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TimestampMixin(CreatedAtMixin, UpdatedAtMixin):
    class Meta:
        abstract = True
