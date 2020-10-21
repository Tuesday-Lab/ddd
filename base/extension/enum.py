from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def values(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def keys(cls):
        return list(map(lambda c: c.name, cls))
