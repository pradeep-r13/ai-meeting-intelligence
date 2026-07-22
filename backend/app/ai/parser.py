from pydantic import BaseModel, Field

from app.ai.exceptions import OutputParserException


def validate_output(
        schema: type[BaseModel],
        data: dict
):
    try:
        return schema.model_validate(data)
    except Exception as e:
        raise OutputParserException(
            f"Failed to parse output: {e}"
        )
