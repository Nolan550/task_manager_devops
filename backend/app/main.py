
from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI(
    title="Task Manager API",
    description="A task management system built while learning Docker and DevOps.",
    version="1.0.0"
)

# Temporary task data
tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "completed": False
    },
    {
        "id": 2,
        "title": "Understand Docker",
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
