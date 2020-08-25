import abc

from ..domain.event import Event
from ..domain.event_repository import EventRepository


class SqlAlchemyEventRepository(EventRepository):

    def create(self, event: Event):
        pass

    def update(self, event: Event):
        pass
