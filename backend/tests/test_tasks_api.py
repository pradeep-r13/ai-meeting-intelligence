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
            "full_name": "Task Owner",
            "password": "123456"
        }
    )

    assert user.status_code == 200

    user_id = user.json()["id"]

    meeting = client.post(
        "/api/v1/meetings/",
        json={
            "title": "Task Meeting",
            "description": "Testing Task Module",
            "owner_id": user_id,
            "meeting_date": "2026-07-18T10:00:00"
        }
    )

    assert meeting.status_code == 200

    return meeting.json()["id"]


def test_create_task():

    meeting_id = create_meeting()

    response = client.post(
        "/api/v1/tasks/",
        json={
            "meeting_id": meeting_id,
            "title": "Prepare Sprint Report",
            "description": "Complete report before Friday",
            "assigned_to": "Pradeep",
            "priority": "high",
            "status": "pending"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Prepare Sprint Report"
    assert data["priority"] == "high"


def test_get_tasks():

    response = client.get(
        "/api/v1/tasks/"
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list
    )


def test_get_task():

    meeting_id = create_meeting()

    create_response = client.post(
        "/api/v1/tasks/",
        json={
            "meeting_id": meeting_id,
            "title": "Deploy Backend",
            "description": "Deploy to production",
            "assigned_to": "DevOps",
            "priority": "medium"
        }
    )

    task_id = create_response.json()["id"]

    response = client.get(
        f"/api/v1/tasks/{task_id}"
    )

    assert response.status_code == 200

    assert response.json()["id"] == task_id


def test_update_task():

    meeting_id = create_meeting()

    create_response = client.post(
        "/api/v1/tasks/",
        json={
            "meeting_id": meeting_id,
            "title": "Old Task",
            "description": "Old Description"
        }
    )

    task_id = create_response.json()["id"]

    response = client.put(
        f"/api/v1/tasks/{task_id}",
        json={
            "title": "Updated Task",
            "priority": "low",
            "status": "completed"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Updated Task"
    assert data["priority"] == "low"
    assert data["status"] == "completed"


def test_delete_task():

    meeting_id = create_meeting()

    create_response = client.post(
        "/api/v1/tasks/",
        json={
            "meeting_id": meeting_id,
            "title": "Delete Task",
            "description": "Delete this task"
        }
    )

    task_id = create_response.json()["id"]

    response = client.delete(
        f"/api/v1/tasks/{task_id}"
    )

    assert response.status_code == 200

    assert response.json()["message"] == "Task deleted successfully"
