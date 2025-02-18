from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .author import Author
from .publisher import Publisher
from .base import Base


book_authors = Table(
    "book_authors",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", ForeignKey("book.id", ondelete="CASCADE")),
    Column("author_id", ForeignKey("author.id", ondelete="RESTRICT")),
)


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    publisher_id: Mapped[int] = mapped_column(ForeignKey("publisher.id"))
    publisher: Mapped[Publisher] = relationship()
    authors: Mapped[List[Author]] = relationship(Author,
                                                 secondary=book_authors,
                                                 cascade="all, delete",
                                                 passive_deletes=True)
