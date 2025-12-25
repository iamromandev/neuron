from typing import Any

from pydantic import HttpUrl
from tortoise import fields

from src.core.base import Base
from src.data.type import ProviderStatus
from src.data.validator import UrlValidator


class Provider(Base):
    status: ProviderStatus = fields.CharEnumField(
        enum_type=ProviderStatus,
        default=ProviderStatus.ACTIVE,
    )
    name: str = fields.CharField(max_length=64, unique=True)
    slug: str = fields.CharField(max_length=64, unique=True)

    base_url: HttpUrl | None = fields.CharField(max_length=128, null=True, validators=[UrlValidator])

    meta: dict[str, Any] | list[Any] | None = fields.JSONField(null=True)

    class Meta:
        ordering = ["-created_at"]
        table = "provider"
        table_description = "Provider"

    def __str__(self) -> str:
        return f"[{self._tag}:__str__(): status {self.status}, name {self.name}, slug {self.slug}]"
