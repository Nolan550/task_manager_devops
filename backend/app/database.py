
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Load environment variables from the project root
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)


class Base(DeclarativeBase):
    pass


def create_database_engine(database_name=None):
    database_url = URL.create(
        drivername="postgresql+psycopg",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "5432")),
        database=database_name or os.getenv("DB_NAME"),
    )

    return create_engine(database_url, echo=True)


engine = create_database_engine()

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
