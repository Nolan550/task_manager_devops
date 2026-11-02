from pydantic import BaseModel, ConfigDict


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    priority: str = "medium"


class TaskUpdate(BaseModel):
    title: str
    description: str = ""
    priority: str = "medium"
    completed: bool


class Task(TaskCreate):
    id: int
    completed: bool

    model_config = ConfigDict(from_attributes=True)