from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app=app)


def test_root_main():
    response = client.get("/")
    # print(response.json().get("urls"))
    print(response.json())
    assert response.json().get("Greetings") == "Hello World!"
    assert response.status_code == 200
