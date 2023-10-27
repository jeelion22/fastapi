from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker, Session
import os

db_username = os.getenv("DB_USER")
db_password = os.getenv("DB_PWD")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{db_username}:{db_password}@localhost/fastapi"
)

engine = create_engine(url=SQLALCHEMY_DATABASE_URL, echo=False)

SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
