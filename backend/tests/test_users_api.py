from fastapi.testclient import TestClient
from app.main import app
import uuid


client = TestClient(app)


def generate_email():
    return f"user_{uuid.uuid4()}@gmail.com"


def test_create_user():

    response = client.post(
        "/api/v1/users/",
        json={
            "email": generate_email(),
            "full_name": "Test User",
            "password": "123456"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert data["full_name"] == "Test User"


def test_get_users():

    response = client.get(
        "/api/v1/users/"
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list
    )


def test_get_user_by_id():

    create_response = client.post(
        "/api/v1/users/",
        json={
            "email": generate_email(),
            "full_name": "ID User",
            "password": "123456"
        }
    )

    assert create_response.status_code == 200

    user_id = create_response.json()["id"]

    response = client.get(
        f"/api/v1/users/{user_id}"
    )

    assert response.status_code == 200

    assert response.json()["id"] == user_id


def test_update_user():

    create_response = client.post(
        "/api/v1/users/",
        json={
            "email": generate_email(),
            "full_name": "Old Name",
            "password": "123456"
        }
    )

    user_id = create_response.json()["id"]

    response = client.put(
        f"/api/v1/users/{user_id}",
        json={
            "full_name": "New Name"
        }
    )

    assert response.status_code == 200

    assert response.json()["full_name"] == "New Name"


def test_delete_user():

    create_response = client.post(
        "/api/v1/users/",
        json={
            "email": generate_email(),
            "full_name": "Delete User",
            "password": "123456"
        }
    )

    user_id = create_response.json()["id"]

    response = client.delete(
        f"/api/v1/users/{user_id}"
    )

    assert response.status_code == 200

    assert response.json()["message"] == "User deleted successfully"
