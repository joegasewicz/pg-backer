import enum
from datetime import datetime

from sqlalchemy import String, ForeignKey, DateTime, func, Enum, Integer
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Model


class DumpStatus(enum.Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    PAUSED = "PAUSED"


class Dump(Model):
    __tablename__ = "dumps"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    database_id: Mapped[int] = mapped_column(ForeignKey("databases.id"), index=True)
    created_on: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_on: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
    completed_on: Mapped[datetime] = mapped_column(DateTime)
    status: Mapped[DumpStatus] = mapped_column(Enum(DumpStatus), nullable=False, default=DumpStatus.PENDING)
    file_path: Mapped[str] = mapped_column(String, nullable=False)
    interval: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f"<Dump database_id={self.database_id} />"
