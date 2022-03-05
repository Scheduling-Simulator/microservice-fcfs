from pydantic import BaseModel


class TaskModel(BaseModel):
    executionTime: int
    period: int
    arrivalTime: int
    deadline: int
