from typing import TypedDict, Optional


class MeetingState(TypedDict):

    # Original transcript
    transcript: str

    # Summary Agent output
    summary: Optional[dict]

    # Decision Agent output
    decisions: Optional[dict]

    # Task Agent output
    tasks: Optional[dict]

    # Verification Agent output
    verification: Optional[dict]
