from tortoise.fields.base import StrEnum


class CostUnit(StrEnum):
    PER_1K = "per_1k"
    PER_10K = "per_10k"


class ModelStatus(StrEnum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    DISABLED = "disabled"


class ModelCapability(StrEnum):
    # Generation modes
    CHAT = "chat"
    COMPLETION = "completion"
    EMBEDDING = "embedding"

    # Output control
    STREAMING = "streaming"
    JSON = "json"
    FUNCTION_CALLING = "function_calling"

    # Modalities
    VISION = "vision"
    AUDIO = "audio"
    VIDEO = "video"

    # Reasoning / behavior
    TOOLS = "tools"
    SYSTEM_PROMPT = "system_prompt"
    TEMPERATURE = "temperature"
    SEED = "seed"

    # Input handling
    LONG_CONTEXT = "long_context"
    FILE_INPUT = "file_input"

    # Performance / infra
    LOW_LATENCY = "low_latency"
    BATCHING = "batching"
    ASYNC = "async"
