class AIException(Exception):
    """Base AI Exception."""


class LLMException(AIException):
    """Exception for LLM-related errors."""


class PromptException(AIException):
    """Exception for prompt-related errors."""


class OutputParserException(AIException):
    """Exception for output parser errors."""


class ModelTimeoutException(AIException):
    """Exception for model timeout errors."""
