from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import get_db, Base
from alembic import command


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"


engine = create_engine(url=SQLALCHEMY_DATABASE_URL)


TestingSessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


@pytest.fixture()
def session():
    print("my session fixture ran")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db

    finally:
        db.close()


@pytest.fixture()
def client(session):
    # print("my client fixture is running")

    def override_get_db():
        try:
            yield session

        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)
