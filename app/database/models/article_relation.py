from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class ArticleRelation(Base):
    __tablename__ = "article_relations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    source_article_id: Mapped[int] = mapped_column(
        ForeignKey("articles.id"),
        nullable=False
    )

    target_article_id: Mapped[int] = mapped_column(
        ForeignKey("articles.id"),
        nullable=False
    )

    relation_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )