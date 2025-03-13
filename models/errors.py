import enum
from datetime import datetime

from sqlalchemy import String, ForeignKey, DateTime, func, Enum
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Model


class Error(Model):
    __tablename__ = "errors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    error: Mapped[String] = mapped_column(String, nullable=False)
    dump_id: Mapped[int] = mapped_column(ForeignKey("dumps.id"), index=True)
    created_on: Mapped[datetime] = mapped_column(DateTime, default=func.now())
