from tortoise.fields.base import StrEnum


class ProviderStatus(StrEnum):
    ACTIVE = "active"
    DEGRADED = "degraded"
    DISABLED = "disabled"
    MAINTENANCE = "maintenance"