from decimal import Decimal
from typing import Any

from tortoise import fields

from src.core.base import Base
from src.core.type import CostUnit, ModelCapability, ModelStatus
from src.data.model.provider import Provider


class Model(Base):
    provider: fields.ForeignKeyRelation["Provider"] = fields.ForeignKeyField(
        model_name="model.Provider",
        related_name="models",
    )
    statuses: list[ModelStatus] = fields.JSONField(default=list)
    capabilities: list[ModelCapability] = fields.JSONField(default=list)
    cost_unit: CostUnit = fields.CharEnumField(
        enum_type=CostUnit,
        default=CostUnit.PER_1K
    )

    name: str = fields.CharField(max_length=64)
    version: str | None = fields.CharField(max_length=32, null=True)

    total_token_limit: int = fields.IntField()
    output_token_limit: int | None = fields.IntField(null=True)
    input_cost: Decimal | None = fields.DecimalField(
        max_digits=10,
        decimal_places=6,
        null=True,
    )
    output_cost: Decimal | None = fields.DecimalField(
        max_digits=10,
        decimal_places=6,
        null=True,
    )

    is_default: bool = fields.BooleanField(default=False)

    meta: dict[str, Any] | list[Any] | None = fields.JSONField(null=True)

    class Meta:
        ordering = ["-created_at"]
        table = "model"
        table_description = "Model"

    def __str__(self) -> str:
        return f"[{self._tag}:__str__(): name {self.name}, version {self.version}]"
