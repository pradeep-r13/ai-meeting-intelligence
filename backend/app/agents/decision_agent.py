from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate


from app.ai.llm import get_llm
from app.ai.schemas import DecisionOutput
from app.ai.prompts import DECISION_PROMPT


parser = PydanticOutputParser(
    pydantic_object=DecisionOutput
)


prompt = ChatPromptTemplate.from_template(
    DECISION_PROMPT
)


llm = get_llm()


async def extract_decisions(
    transcript: str
) -> DecisionOutput:
    """
    Extract decisions from meeting transcript.
    """

    chain = (
        prompt
        | llm
        | parser
    )

    return await chain.ainvoke(
        {
            "transcript": transcript,
            "format_instructions":
            parser.get_format_instructions()
        }
    )
