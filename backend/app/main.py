from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .database import get_db
from . import models
from .schemas import TaskCreate, TaskUpdate, TaskPatch, Task as TaskSchema

app = FastAPI(title="Task Manager API")

def commit_changes(db: Session):
    try:
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="A database error occurred"
        )

@app.get("/")
def root():
    return {"message": "Task Manager API is running"}


@app.post("/tasks", response_model=TaskSchema, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(**task.model_dump())

    db.add(db_task)
    commit_changes(db)
    db.refresh(db_task)

    return db_task


@app.get("/tasks", response_model=list[TaskSchema])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()


@app.get("/tasks/{task_id}", response_model=TaskSchema)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@app.put("/tasks/{task_id}", response_model=TaskSchema)
def update_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in task_data.model_dump().items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task

@app.patch("/tasks/{task_id}", response_model=TaskSchema)
def patch_task(
    task_id: int,
    task_data: TaskPatch,
    db: Session = Depends(get_db)
):
    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    updates = task_data.model_dump(
        exclude_unset=True,
        exclude_none=True
    )

    for key, value in updates.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()