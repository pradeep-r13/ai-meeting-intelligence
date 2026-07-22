from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.ai.llm import get_llm
from app.ai.schemas import TaskOutput
from app.ai.prompts import TASK_PROMPT


parser = PydanticOutputParser(
    pydantic_object=TaskOutput
)

prompt = ChatPromptTemplate.from_template(
    TASK_PROMPT
)

llm = get_llm()


async def extract_tasks(
    transcript: str
) -> TaskOutput:
    """
    Extract action items from meeting transcript.
    """

    chain = (
        prompt
        | llm
        | parser
    )

    return await chain.ainvoke(
        {
            "transcript": transcript,
            "format_instructions": parser.get_format_instructions()
        }
    )
