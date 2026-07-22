import asyncio

from app.agents.verification_agent import verify_meeting_intelligence


transcript = """

Rahul:
We discussed database migration.

Manager:
We have decided to migrate our database from MySQL to PostgreSQL.

The backend team will complete this migration by Friday.

Priya:
I will finish the UI design by Monday.

"""


summary = """
{
    "summary": "The team decided to migrate the database from MySQL to PostgreSQL. Backend migration will be completed by Friday. Priya will finish UI design by Monday."
}
"""


decisions = """
{
    "decisions": [
        {
            "title": "Database Migration",
            "description": "Migrate database from MySQL to PostgreSQL",
            "owner": "backend team",
            "confidence": 0.95
        }
    ]
}
"""


tasks = """
{
    "tasks": [
        {
            "task": "Complete database migration",
            "owner": "backend team",
            "priority": "high",
            "deadline": "Friday"
        },
        {
            "task": "Finish UI design",
            "owner": "Priya",
            "priority": "medium",
            "deadline": "Monday"
        }
    ]
}
"""


async def main():

    result = await verify_meeting_intelligence(
        transcript=transcript,
        summary=summary,
        decisions=decisions,
        tasks=tasks
    )

    print("\n========== VERIFICATION OUTPUT ==========\n")

    print(
        result.model_dump_json(
            indent=4
        )
    )


if __name__ == "__main__":

    asyncio.run(main())
