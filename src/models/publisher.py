from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class Publisher(Base):
    __tablename__ = "publisher"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
