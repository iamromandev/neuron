from enum import Enum
from typing import Any, Optional

from src.core.base import BaseSchema


class Model(str, Enum):
    """Enum for supported LLM models.

    Inheriting from `str` allows the enum members to be treated as strings,
    which is useful for serialization.
    """

    # OpenAI
    GPT_4_OMNI = "gpt-4o"
    GPT_4_TURBO = "gpt-4-turbo"
    GPT_3_5_TURBO = "gpt-3.5-turbo"

    # Anthropic
    CLAUDE_3_OPUS = "claude-3-opus-20240229"
    CLAUDE_3_SONNET = "claude-3-sonnet-20240229"
    CLAUDE_3_HAIKU = "claude-3-haiku-20240307"


class RunSchema(BaseSchema):
    """Schema for running a generic prompt on an LLM."""

    prompt: str
    model: Optional[Model] = None
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 256
    # For any other provider-specific parameters
    extra_params: dict[str, Any] = {}


class RunOutSchema(BaseSchema):
    """Schema for the output of a generic LLM run."""

    output: str
    model: Optional[Model] = None

    class Usage(BaseSchema):
        prompt_tokens: int
        completion_tokens: int
        total_tokens: int

    usage: Optional[Usage] = None
