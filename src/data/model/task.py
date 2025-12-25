from typing import Any

from tortoise import fields

from src.core.base import Base
from src.data.type import TaskStatus

from .run import Run


class Task(Base):
    run: fields.ForeignKeyRelation["Run"] = fields.ForeignKeyField(
        model_name="model.Run",
        related_name="tasks"
    )

    name: str = fields.CharField(max_length=128)

    status: TaskStatus = fields.CharEnumField(
        enum_type=TaskStatus,
        default=TaskStatus.PENDING,
    )

    input_payload: dict[str, Any] = fields.JSONField()
    output_payload: dict[str, Any] | None = fields.JSONField(null=True)

    error: str | None = fields.TextField(null=True)

    meta: dict[str, Any] | list[Any] | None = fields.JSONField(null=True)

    class Meta:
        ordering = ["-created_at"]
        table = "task"
        table_description = "Task"

    def __str__(self) -> str:
        return f"[{self._tag}:__str__(): ]"