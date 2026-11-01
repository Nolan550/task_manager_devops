import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, URL

# Load the .env file from the project root
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

# Read database configuration
database_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", "5432")),
    database=os.getenv("DB_NAME"),
)

# Create SQLAlchemy engine
engine = create_engine(database_url, echo=True)
