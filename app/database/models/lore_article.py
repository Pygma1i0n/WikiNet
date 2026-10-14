from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class LoreArticle(Base):
    __tablename__ = "lore_articles"

    article_id: Mapped[int] = mapped_column(
        ForeignKey("articles.id"),
        primary_key=True
    )