
from datetime import date
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = ""
    priority: Priority = Priority.medium
    due_date: date | None = None


class TaskUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = ""
    priority: Priority = Priority.medium
    completed: bool = False
    due_date: date | None = None


class TaskPatch(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
    priority: Priority | None = None
    completed: bool | None = None
    due_date: date | None = None


class Task(TaskCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    completed: bool
