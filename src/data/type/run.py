from tortoise.fields.base import StrEnum


class OwnerType(StrEnum):
    USER = "user"
    AGENT = "agent"
    SYSTEM = "system"

class RunType(StrEnum):
    CHAT = "chat"
    COMPLETION = "completion"
    AGENT = "agent"
    BATCH = "batch"
    SYSTEM = "system"
    EVAL = "eval"

class RunStatus(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    TIMEOUT = "timeout"