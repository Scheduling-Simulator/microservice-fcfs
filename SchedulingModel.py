from pydantic import BaseModel


class SchedulingModel(BaseModel):
    schedule: list[int]
    lcm: int
