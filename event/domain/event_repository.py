import abc

from ..domain.event import Event


class EventRepository(abc.ABC):

    @abc.abstractmethod
    def create(self, event: Event):
        pass

    @abc.abstractmethod
    def update(self, event: Event):
        pass
