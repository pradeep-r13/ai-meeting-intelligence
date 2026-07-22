import asyncio

from app.agents.summary_agent import generate_summary


transcript = """
Rahul:
Today we reviewed the Q3 roadmap.

Priya:
The authentication module is completed.

Manager:
The database migration has been approved and will start next Monday.

Rahul:
Frontend redesign is still under discussion.

Manager:
Everyone should finish the pending tasks before Friday.
"""


async def main():

    result = await generate_summary(transcript)

    print("\n========== SUMMARY ==========\n")

    print(result.model_dump_json(indent=4))


if __name__ == "__main__":
    asyncio.run(main())
