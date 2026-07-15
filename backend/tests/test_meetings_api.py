from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def generate_email():
    return f"user_{uuid4()}@gmail.com"


def create_user():

    response = client.post(
        "/api/v1/users/",
        json={
            "email": generate_email(),
            "full_name": "Meeting Owner",
            "password": "123456"
        }
    )

    assert response.status_code == 200

    return response.json()["id"]


def test_create_meeting():

    owner_id = create_user()

    response = client.post(
        "/api/v1/meetings/",
        json={
            "title": "Sprint Planning",
            "description": "Weekly planning meeting",
            "owner_id": owner_id,
            "meeting_date": "2026-07-16T10:00:00"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Sprint Planning"


def test_get_meetings():

    response = client.get(
        "/api/v1/meetings/"
    )

    assert response.status_code == 200

    assert isinstance(response.json(), list)


def test_get_meeting():

    owner_id = create_user()

    create_response = client.post(
        "/api/v1/meetings/",
        json={
            "title": "Daily Standup",
            "description": "Daily meeting",
            "owner_id": owner_id,
            "meeting_date": "2026-07-16T09:00:00"
        }
    )

    meeting_id = create_response.json()["id"]

    response = client.get(
        f"/api/v1/meetings/{meeting_id}"
    )

    assert response.status_code == 200

    assert response.json()["id"] == meeting_id


def test_update_meeting():

    owner_id = create_user()

    create_response = client.post(
        "/api/v1/meetings/",
        json={
            "title": "Old Meeting",
            "description": "Old Description",
            "owner_id": owner_id,
            "meeting_date": "2026-07-16T10:00:00"
        }
    )

    meeting_id = create_response.json()["id"]

    response = client.put(
        f"/api/v1/meetings/{meeting_id}",
        json={
            "title": "New Meeting"
        }
    )

    assert response.status_code == 200

    assert response.json()["title"] == "New Meeting"


def test_delete_meeting():

    owner_id = create_user()

    create_response = client.post(
        "/api/v1/meetings/",
        json={
            "title": "Delete Meeting",
            "description": "Delete",
            "owner_id": owner_id,
            "meeting_date": "2026-07-16T10:00:00"
        }
    )

    meeting_id = create_response.json()["id"]

    response = client.delete(
        f"/api/v1/meetings/{meeting_id}"
    )

    assert response.status_code == 200

    assert response.json()["message"] == "Meeting deleted successfully"
