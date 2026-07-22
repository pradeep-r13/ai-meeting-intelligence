import asyncio

from app.agents.task_agent import extract_tasks


transcript = """
Rahul:
Backend API should be completed by Friday.

Priya:
I will finish the UI design by Monday.

Manager:
Aman will perform integration testing next week.

The database migration has already been approved.
"""


async def main():

    result = await extract_tasks(transcript)

    print("\n========== TASK OUTPUT ==========\n")

    print(result.model_dump_json(indent=4))


if __name__ == "__main__":
    asyncio.run(main())
