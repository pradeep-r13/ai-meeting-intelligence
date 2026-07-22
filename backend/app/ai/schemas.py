from pydantic import BaseModel, Field


class SummaryOutput(BaseModel):
    summary: str = Field(
        ...,
        description="The generated summary text"
    )


class DecisionItem(BaseModel):

    title: str = Field(
        ...,
        description="Decision title"
    )

    description: str = Field(
        ...,
        description="Decision explanation"
    )

    owner: str | None = Field(
        default=None,
        description="Person responsible for decision"
    )

    confidence: float = Field(
        default=0.0,
        description="Confidence score between 0 and 1"
    )


class DecisionOutput(BaseModel):

    decisions: list[DecisionItem] = Field(
        ...,
        description="Extracted meeting decisions"
    )


class TaskItem(BaseModel):

    task: str = Field(
        ...,
        description="Task description"
    )

    owner: str | None = None

    priority: str = "medium"

    deadline: str | None = None


class TaskOutput(BaseModel):

    tasks: list[TaskItem] = Field(
        ...,
        description="Generated list of tasks"
    )
