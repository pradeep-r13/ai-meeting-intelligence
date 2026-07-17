from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def generate_email():
    return f"user_{uuid4()}@gmail.com"


def create_meeting():

    user = client.post(
        "/api/v1/users/",
        json={
            "email": generate_email(),
            "full_name": "Decision Owner",
            "password": "123456"
        }
    )

    assert user.status_code == 200

    user_id = user.json()["id"]

    meeting = client.post(
        "/api/v1/meetings/",
        json={
            "title": "Decision Meeting",
            "description": "Testing Decision Module",
            "owner_id": user_id,
            "meeting_date": "2026-07-18T10:00:00"
        }
    )

    assert meeting.status_code == 200

    return meeting.json()["id"]


def test_create_decision():

    meeting_id = create_meeting()

    response = client.post(
        "/api/v1/decisions/",
        json={
            "meeting_id": meeting_id,
            "title": "Use FastAPI",
            "description": "Backend will be built using FastAPI",
            "decision_by": "Tech Lead",
            "priority": "high",
            "status": "approved"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Use FastAPI"
    assert data["priority"] == "high"


def test_get_decisions():

    response = client.get(
        "/api/v1/decisions/"
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list
    )


def test_get_decision():

    meeting_id = create_meeting()

    create = client.post(
        "/api/v1/decisions/",
        json={
            "meeting_id": meeting_id,
            "title": "Cloud",
            "description": "Deploy on AWS",
            "decision_by": "Manager",
            "priority": "medium",
            "status": "pending"
        }
    )

    decision_id = create.json()["id"]

    response = client.get(
        f"/api/v1/decisions/{decision_id}"
    )

    assert response.status_code == 200

    assert response.json()["id"] == decision_id


def test_update_decision():

    meeting_id = create_meeting()

    create = client.post(
        "/api/v1/decisions/",
        json={
            "meeting_id": meeting_id,
            "title": "Old Title",
            "description": "Old Description",
            "decision_by": "CEO",
            "priority": "low",
            "status": "pending"
        }
    )

    decision_id = create.json()["id"]

    response = client.put(
        f"/api/v1/decisions/{decision_id}",
        json={
            "title": "New Title",
            "priority": "high",
            "status": "approved"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "New Title"
    assert data["priority"] == "high"
    assert data["status"] == "approved"


def test_delete_decision():

    meeting_id = create_meeting()

    create = client.post(
        "/api/v1/decisions/",
        json={
            "meeting_id": meeting_id,
            "title": "Delete Me",
            "description": "Temporary Decision",
            "decision_by": "Admin",
            "priority": "medium",
            "status": "pending"
        }
    )

    decision_id = create.json()["id"]

    response = client.delete(
        f"/api/v1/decisions/{decision_id}"
    )

    assert response.status_code == 200

    assert response.json()["message"] == "Decision deleted successfully"
