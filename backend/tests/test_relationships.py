from app.database.models import (Meeting)
from app.database.models import (User)


def test_meeting_relationships():

    assert hasattr(Meeting, 'transcripts')
    assert hasattr(Meeting, 'decisions')
    assert hasattr(Meeting, 'tasks')
    assert hasattr(User, 'meeting')
