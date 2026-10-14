from sqlalchemy import ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Rating(Base):
    __tablename__ = "ratings"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    article_id: Mapped[int] = mapped_column(
        ForeignKey("articles.id"),
        nullable=False
    )

    value: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "article_id",
            name="uq_user_article_rating"
        ),
    )