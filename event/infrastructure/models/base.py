from django.db import models


class CreatedAtMixin(object):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class UpdatedAtMixin(object):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TimestampMixin(CreatedAtMixin, UpdatedAtMixin):
    pass
