from app.workflow.state import MeetingState

from app.agents.summary_agent import generate_summary
from app.agents.decision_agent import extract_decisions
from app.agents.task_agent import extract_tasks
from app.agents.verification_agent import verify_meeting_intelligence


async def summary_node(
    state: MeetingState
) -> MeetingState:
    """
    Summary Agent Node
    """

    result = await generate_summary(
        state["transcript"]
    )

    state["summary"] = (
        result.model_dump()
    )

    return state


async def decision_node(
    state: MeetingState
) -> MeetingState:
    """
    Decision Agent Node
    """

    result = await extract_decisions(
        state["transcript"]
    )

    state["decisions"] = (
        result.model_dump()
    )

    return state


async def task_node(
    state: MeetingState
) -> MeetingState:
    """
    Task Agent Node
    """

    result = await extract_tasks(
        state["transcript"]
    )

    state["tasks"] = (
        result.model_dump()
    )

    return state


async def verification_node(
    state: MeetingState
) -> MeetingState:
    """
    Verification Agent Node
    """

    result = await verify_meeting_intelligence(
        transcript=state["transcript"],

        summary=str(
            state["summary"]
        ),

        decisions=str(
            state["decisions"]
        ),

        tasks=str(
            state["tasks"]
        )
    )

    state["verification"] = (
        result.model_dump()
    )

    return state
