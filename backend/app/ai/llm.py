from functools import lru_cache

import os

from langchain_core.language_models.chat_models import BaseChatModel

from langchain_groq import ChatGroq

from app.core.config import settings

from app.ai.config import (
    DEFAULT_MODEL,
    TEMPERATURE,
    MAX_TOKENS,
    TIMEOUT,
    MAX_RETRIES
)


class LLMFactory:
    """
    Factory class responsible for creating LLM clients.

    Supported Providers:
    - Groq
    - Ollama (Future)
    - OpenAI (Future)
    - Azure OpenAI (Future)
    """

    @staticmethod
    def groq() -> BaseChatModel:

        return ChatGroq(
            model=settings.GROQ_MODEL or DEFAULT_MODEL,
            api_key=settings.GROQ_API_KEY,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            timeout=TIMEOUT,
            max_retries=MAX_RETRIES,
        )


@lru_cache(maxsize=1)
def get_llm() -> BaseChatModel:
    """
    Returns singleton LLM instance.
    """

    return LLMFactory.groq()
