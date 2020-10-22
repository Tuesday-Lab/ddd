from django.db import transaction

from event.models import Event, Money, Currency


class EventService:

    @transaction.atomic
    def create(self, title: str,
               slug: str,
               kind: str,
               amount: float,
               currency: Currency,
               max_attendee_count: str,
               description: str
               ):
        if self._is_exists_duplicate_slug(slug):
            #  TODO custom error handling
            raise ValueError("already exist slug")
        event = Event.objects.create_new(
            title=title,
            slug=slug,
            kind=kind,
            money=Money(amount=amount,
                        currency=currency),
            max_attendee_count=max_attendee_count,
            description=description

        )
        return event

    def _is_exists_duplicate_slug(self, slug):
        return Event.objects.filter(slug=slug).exists()


service = EventService()
