from datetime import datetime

from pydantic import root_validator
from pydantic.main import BaseModel


class Schedule(BaseModel):
    start_time: datetime = None
    end_time: datetime = None

    @root_validator
    def check_time(cls, values):
        start_time, end_time = values.get('start_time'), values.get('end_time')
        if start_time and end_time and start_time >= end_time:
            raise ValueError("start_time should be grater than end_time")
        if not start_time and end_time:
            raise ValueError("start_time should be exist with end_time")
        return values
