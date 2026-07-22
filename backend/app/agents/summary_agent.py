from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.ai.llm import get_llm
from app.ai.schemas import SummaryOutput
from app.ai.prompts import SUMMARY_PROMPT


parser = PydanticOutputParser(
    pydantic_object=SummaryOutput
)


prompt = ChatPromptTemplate.from_template(
    SUMMARY_PROMPT
)


llm = get_llm()


async def generate_summary(
    transcript: str
) -> SummaryOutput:
    """
    Generate executive summary from transcript.
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
