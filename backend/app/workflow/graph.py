from langgraph.graph import StateGraph, START, END

from app.workflow.state import MeetingState

from app.workflow.nodes import (
    summary_node,
    decision_node,
    task_node,
    verification_node
)


def build_meeting_graph():
    """
    Build Meeting Intelligence LangGraph workflow.
    """

    graph = StateGraph(
        MeetingState
    )

    # Register Nodes

    graph.add_node(
        "summary",
        summary_node
    )

    graph.add_node(
        "decision",
        decision_node
    )

    graph.add_node(
        "task",
        task_node
    )

    graph.add_node(
        "verification",
        verification_node
    )

    # Define Workflow Flow

    graph.add_edge(
        START,
        "summary"
    )

    graph.add_edge(
        "summary",
        "decision"
    )

    graph.add_edge(
        "decision",
        "task"
    )

    graph.add_edge(
        "task",
        "verification"
    )

    graph.add_edge(
        "verification",
        END
    )

    return graph.compile()


meeting_graph = build_meeting_graph()
