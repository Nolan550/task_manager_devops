from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI(
    title="Task Manager API",
    description="A task management system built while learning Docker and DevOps.",
    version="1.0.0"
)


# Data supplied by the client when creating a task
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    priority: Literal["low", "medium", "high"] = "medium"


# Complete task structure, including system-generated fields
class Task(TaskCreate):
    id: int
    completed: bool = False


# Temporary in-memory storage
tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "description": "Understand API development",
        "priority": "high",
        "completed": False
    },
    {
        "id": 2,
        "title": "Understand Docker",
        "description": "Learn containers and images",
        "priority": "medium",
        "completed": False
    }
]


@app.get("/")
def home():
    return {
        "message": "Welcome to Task Manager API",
        "status": "running"
    }


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_data: TaskCreate):

    new_id = max(
        (task["id"] for task in tasks),
        default=0
    ) + 1

    new_task = Task(
        id=new_id,
        **task_data.model_dump()
    )

    tasks.append(new_task.model_dump())

    return new_task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_data: TaskUpdate):

    for index, task in enumerate(tasks):

        if task["id"] == task_id:

            updated_task = Task(
                id=task_id,
                **updated_data.model_dump()
            )

            tasks[index] = updated_task.model_dump()

            return updated_task

    return {"error": "Task not found"}

class TaskUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    priority: Literal["low", "medium", "high"] = "medium"
    completed: bool = False


