from datetime import datetime
from typing import Optional

from django.contrib.auth.models import User
from django.db import transaction

from base.exceptions import ConflictResource
from event.models import Event
from event.vo import Currency, Money, Schedule


class EventService:

    @transaction.atomic
    def create(self, title: str,
               slug: str,
               kind: str,
               amount: float,
               currency: Currency,
               max_attendee_count: Optional[int],
               description: str,
               user: User,
               start_time: datetime = None,
               end_time: datetime = None,
               ):
        if self._is_exists_duplicate_slug(slug):
            raise ConflictResource(detail="duplicate slug")

        event = Event.objects.create_new(
            title=title,
            slug=slug,
            kind=kind,
            money=Money(amount=amount,
                        currency=currency),
            max_attendee_count=max_attendee_count,
            description=description,
            user=user,
            schedule=Schedule(start_time=start_time, end_time=end_time)

        )
        return event

    def _is_exists_duplicate_slug(self, slug):
        return Event.objects.filter(slug=slug).exists()


service = EventService()
