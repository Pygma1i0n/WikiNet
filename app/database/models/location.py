from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Location(Base):
    __tablename__ = "locations"

    article_id: Mapped[int] = mapped_column(
        ForeignKey("articles.id"),
        primary_key=True
    )

    level: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    parent_location_id: Mapped[int | None] = mapped_column(
        ForeignKey("locations.article_id"),
        nullable=True
    )