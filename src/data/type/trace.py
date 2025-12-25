from tortoise.fields.base import StrEnum


class TraceLevel(StrEnum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    DEBUG = "debug"
    METRIC = "metric"