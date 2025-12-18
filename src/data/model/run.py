import uuid
from typing import Any

from tortoise import fields

from src.core.base import Base
from src.core.type import OwnerType, RunStatus, RunType


class Run(Base):
    type: RunType = fields.CharEnumField(
        enum_type=RunType,
        default=RunType.CHAT
    )
    status: RunStatus = fields.CharEnumField(
        enum_type=RunStatus,
        default=RunStatus.PENDING,
    )
    owner_type: OwnerType = fields.CharEnumField(
        enum_type=OwnerType,
        default=OwnerType.USER,
    )
    owner_id: uuid.UUID | None = fields.UUIDField(
        null=True
    )

    entrypoint: str = fields.CharField(max_length=128)

    input_payload: dict[str, Any] = fields.JSONField()
    output_payload: dict[str, Any] | None = fields.JSONField(null=True)

    error: str | None = fields.TextField(null=True)

    meta: dict[str, Any] | list[Any] | None = fields.JSONField(null=True)

    class Meta:
        ordering = ["-created_at"]
        table = "run"
        table_description = "Run"

    def __str__(self) -> str:
        return f"[{self._tag}:__str__(): ]"
