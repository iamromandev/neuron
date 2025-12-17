from typing import Any

from tortoise import fields

from src.core.base import Base


class Provider(Base):
    name: str = fields.CharField(max_length=64, unique=True)
    slug: str = fields.CharField(max_length=64, unique=True)

    meta: dict[str, Any] | list[Any] | None = fields.JSONField(null=True)

    class Meta:
        ordering = ["-created_at"]
        table = "provider"
        table_description = "Provider"

    def __str__(self) -> str:
        return f"[{self._tag}:__str__(): name {self.name}, slug {self.slug}]"
