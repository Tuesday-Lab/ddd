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
        #  TODO: vo와 model을 어떻게 조화시킬수 있을지 고민해보기..
        money = Money(amount=amount,
                      currency=currency)

        event = Event.objects.create(
            title=title,
            slug=slug,
            kind=kind,
            amount=money.amount,
            currency=money.currency,
            max_attendee_count=max_attendee_count,
            description=description

        )
        return event

    def _is_exists_duplicate_slug(self, slug):
        return Event.objects.filter(slug=slug).exists()


service = EventService()
