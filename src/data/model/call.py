from decimal import Decimal
from typing import Any

from tortoise import fields

from src.core.base import Base

from ..type import CallStatus
from .model import Model
from .provider import Provider
from .task import Task


class Call(Base):
    provider: fields.ForeignKeyRelation["Provider"] = fields.ForeignKeyField(
        model_name="model.Provider",
        related_name="calls",
        on_delete=fields.RESTRICT
    )
    model: fields.ForeignKeyRelation["Model"] = fields.ForeignKeyField(
        model_name="model.Model",
        related_name="calls",
        on_delete=fields.RESTRICT
    )
    task: fields.ForeignKeyRelation["Task"] = fields.ForeignKeyField(
        model_name="model.Task",
        related_name="calls",
    )
    status: CallStatus = fields.CharEnumField(
        enum_type=CallStatus,
        default=CallStatus.PENDING,
    )

    prompt_tokens: int | None = fields.IntField(null=True)
    output_tokens: int | None = fields.IntField(null=True)
    total_tokens: int | None = fields.IntField(null=True)

    cost: Decimal | None = fields.DecimalField(
        max_digits=12,
        decimal_places=6,
        null=True,
    )

    input_payload: dict[str, Any] = fields.JSONField()
    output_payload: dict[str, Any] | None = fields.JSONField(null=True)

    latency_ms: int | None = fields.IntField(null=True)

    error: str | None = fields.TextField(null=True)

    meta: dict[str, Any] | list[Any] | None = fields.JSONField(null=True)

    class Meta:
        ordering = ["-created_at"]
        table = "call"
        table_description = "Call"

    def __str__(self) -> str:
        return f"[{self._tag}:__str__(): ]"
