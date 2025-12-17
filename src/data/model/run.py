import uuid

from tortoise import fields

from src.core.base import Base
from src.core.type import OwnerType, RunStatus, RunType


class Run(Base):
    type: RunType = fields.CharEnumField(
        enum_type=RunType,
        default=RunType.CHAT,
    )
    status: RunStatus = fields.CharEnumField(
        RunStatus,
        default=RunStatus.PENDING,
    )
    owner_type: OwnerType = fields.CharEnumField(
        enum_type=OwnerType,
        default=OwnerType.USER,
    )
    owner_id : uuid.UUID| None = fields.UUIDField(
        null=True
    )