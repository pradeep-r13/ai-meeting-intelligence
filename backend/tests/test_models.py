from app.database.models import (
    User,
    Meeting,
    Decision,
    Transcript,
    Task
)


def test_models_import():

    assert User is not None
    assert Meeting is not None
    assert Transcript is not None
    assert Decision is not None
    assert Task is not None
