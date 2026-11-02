from app.database import SessionLocal
from app.models import Task

# Open a database session
db = SessionLocal()

try:
    # Create a new task
    new_task = Task(
        title="Learn SQLAlchemy",
        description="Understand ORM and database sessions",
        priority="high",
        completed=False
    )

    # Add task to the session
    db.add(new_task)

    # Save changes to PostgreSQL
    db.commit()

    # Retrieve the generated ID
    db.refresh(new_task)

    print("Task created successfully!")
    print(f"Task ID: {new_task.id}")
    print(f"Task title: {new_task.title}")

except Exception as error:
    db.rollback()
    print(f"Database operation failed: {error}")

finally:
    db.close()