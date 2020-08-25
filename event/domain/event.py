from dataclasses import dataclass
from datetime import datetime


@dataclass
class Host:
    id: int
    name: str


@dataclass
class Price:
    amount: float
    currency: str


@dataclass
class Category:
    id: int
    name: str


@dataclass
class Schedule:
    start_time: datetime
    end_time: datetime


@dataclass
class Event:
    host: Host
    price: Price
    category: Category
    schedule: Schedule
