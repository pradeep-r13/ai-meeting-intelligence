from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.ai.llm import get_llm
from app.ai.schemas import VerificationOutput
from app.ai.prompts import VERIFICATION_PROMPT


parser = PydanticOutputParser(
    pydantic_object=VerificationOutput
)


prompt = ChatPromptTemplate.from_template(
    VERIFICATION_PROMPT
)


llm = get_llm()


async def verify_meeting_intelligence(
    transcript: str,
    summary: str,
    decisions: str,
    tasks: str
) -> VerificationOutput:
    """
    Verify AI generated meeting intelligence.

    Checks:
    - Summary accuracy
    - Decision validity
    - Task correctness
    - Hallucination detection
    """

    chain = (
        prompt
        | llm
        | parser
    )

    return await chain.ainvoke(
        {
            "transcript": transcript,

            "summary": summary,

            "decisions": decisions,

            "tasks": tasks,

            "format_instructions":
                parser.get_format_instructions()
        }
    )
