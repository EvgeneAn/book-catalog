import datetime
from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class Author(Base):
    __tablename__ = "author"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(100), nullable=True)
    birthday: Mapped[datetime.date] = mapped_column(Date, nullable=True)
