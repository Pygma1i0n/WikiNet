from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Character(Base):
    __tablename__ = "characters"

    article_id: Mapped[int] = mapped_column(
        ForeignKey("articles.id"),
        primary_key=True
    )

    race: Mapped[str | None] = mapped_column(
        String(100)
    )

    faction: Mapped[str | None] = mapped_column(
        String(100)
    )

    gender: Mapped[str | None] = mapped_column(
        String(30)
    )

    character_status: Mapped[str | None] = mapped_column(
        String(50)
    )