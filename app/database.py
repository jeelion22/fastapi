from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker, Session

# import os

# db_username = os.getenv("DB_USER")
# db_password = os.getenv("DB_PWD")
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"


engine = create_engine(url=SQLALCHEMY_DATABASE_URL, echo=False)

SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
