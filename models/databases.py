from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Model


class Database(Model):
    __tablename__ = "databases"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    db_name: Mapped[str] = mapped_column(String(64), nullable=False)
    host: Mapped[str] = mapped_column(String(64), nullable=False)
    port: Mapped[int] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(String(64))
    password: Mapped[str] = mapped_column(String(64))
    url: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f"<Database db_name={self.db_name} />"
