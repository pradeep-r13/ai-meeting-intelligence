import asyncio

from app.workflow.graph import meeting_graph


transcript = """

Rahul:
Today we discussed the backend roadmap.

Manager:
We have decided to migrate our database from MySQL to PostgreSQL.

The backend team will complete the migration by Friday.

Priya:
I will finish the UI redesign by Monday.

Manager:
Aman will perform integration testing next week.

"""


async def main():

    initial_state = {

        "transcript": transcript,

        "summary": None,

        "decisions": None,

        "tasks": None,

        "verification": None
    }

    result = await meeting_graph.ainvoke(
        initial_state
    )

    print("\n========== FINAL WORKFLOW OUTPUT ==========\n")

    print(result)


if __name__ == "__main__":

    asyncio.run(main())
