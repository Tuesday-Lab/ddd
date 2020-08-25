from django.db import transaction

from ..domain.event import Event
from ..infrastructure.sqlalchemy_event_repository import SqlAlchemyEventRepository


class EventApplication:
    @transaction.atomic
    def create(self, event: Event):
        repo = SqlAlchemyEventRepository()  # Todo DI
        repo.create(event)
        return event
