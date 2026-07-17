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
            "full_name": "Meeting Owner",
            "password": "123456"
        }
    )

    assert user.status_code == 200

    user_id = user.json()["id"]

    meeting = client.post(
        "/api/v1/meetings/",
        json={
            "title": "Transcript Meeting",
            "description": "Testing Transcript",
            "owner_id": user_id,
            "meeting_date": "2026-07-16T10:00:00Z"
        }
    )

    assert meeting.status_code == 200

    return meeting.json()["id"]


def test_create_transcript():

    meeting_id = create_meeting()

    response = client.post(
        "/api/v1/transcripts/",
        json={
            "meeting_id": meeting_id,
            "speaker": "Speaker 1",
            "content": "Hello everyone",
            "start_time": 0.0,
            "end_time": 5.2
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["speaker"] == "Speaker 1"


def test_get_transcripts():

    response = client.get(
        "/api/v1/transcripts/"
    )

    assert response.status_code == 200

    assert isinstance(response.json(), list)


def test_get_transcript():

    meeting_id = create_meeting()

    create = client.post(
        "/api/v1/transcripts/",
        json={
            "meeting_id": meeting_id,
            "speaker": "Speaker 2",
            "content": "Testing",
            "start_time": 1,
            "end_time": 4
        }
    )

    transcript_id = create.json()["id"]

    response = client.get(
        f"/api/v1/transcripts/{transcript_id}"
    )

    assert response.status_code == 200

    assert response.json()["id"] == transcript_id


def test_update_transcript():

    meeting_id = create_meeting()

    create = client.post(
        "/api/v1/transcripts/",
        json={
            "meeting_id": meeting_id,
            "speaker": "Speaker",
            "content": "Old Content",
            "start_time": 0,
            "end_time": 2
        }
    )

    transcript_id = create.json()["id"]

    response = client.put(
        f"/api/v1/transcripts/{transcript_id}",
        json={
            "content": "Updated Content"
        }
    )

    assert response.status_code == 200

    assert response.json()["content"] == "Updated Content"


def test_delete_transcript():

    meeting_id = create_meeting()

    create = client.post(
        "/api/v1/transcripts/",
        json={
            "meeting_id": meeting_id,
            "speaker": "Speaker",
            "content": "Delete Me",
            "start_time": 0,
            "end_time": 3
        }
    )

    transcript_id = create.json()["id"]

    response = client.delete(
        f"/api/v1/transcripts/{transcript_id}"
    )

    assert response.status_code == 200

    assert response.json()["message"] == "Transcript deleted successfully"
