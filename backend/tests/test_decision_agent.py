import asyncio

from app.agents.decision_agent import extract_decisions


transcript = """

Rahul:
We discussed database migration.

Manager:
We have decided to migrate our database from MySQL to PostgreSQL.

The backend team will complete this migration by Friday.

Priya:
Frontend redesign is only a suggestion, not finalized.

"""


async def main():

    result = await extract_decisions(
        transcript
    )

    print("\n========== DECISION OUTPUT ==========\n")

    print(
        result.model_dump_json(
            indent=4
        )
    )


if __name__ == "__main__":

    asyncio.run(main())
