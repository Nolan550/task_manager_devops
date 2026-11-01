from sqlalchemy import text
from app.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_user, current_database()")
        )

        user, database = result.fetchone()

        print("Database connection successful!")
        print(f"Connected user: {user}")
        print(f"Connected database: {database}")

except Exception as error:
    print("Database connection failed!")
    print(error)
