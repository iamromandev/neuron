from datetime import datetime
from typing import Any

from tortoise import fields

from src.core.base import Base
from src.data.type import TraceLevel

from .call import Call
from .run import Run
from .task import Task


class Trace(Base):
    run: fields.ForeignKeyRelation["Run"] = fields.ForeignKeyField(
        model_name="model.Run",
        related_name="traces"
    )
    task: fields.ForeignKeyRelation["Task"] = fields.ForeignKeyField(
        model_name="model.Task",
        related_name="traces",
        on_delete=fields.SET_NULL,
        null=True
    )
    call: fields.ForeignKeyRelation["Call"] = fields.ForeignKeyField(
        model_name="model.Call",
        related_name="traces",
        on_delete=fields.SET_NULL,
        null=True
    )
    level: TraceLevel = fields.CharEnumField(
        enum_type=TraceLevel,
        default=TraceLevel.INFO
    )

    message: str = fields.TextField()
    timestamp: datetime = fields.DatetimeField(auto_now_add=True)

    meta: dict[str, Any] | list[Any] | None = fields.JSONField(null=True)

    class Meta:
        ordering = ["-created_at"]
        table = "trace"
        table_description = "Trace"

    def __str__(self) -> str:
        return f"[{self._tag}:__str__(): level {self.level}, message {self.message}]"
