from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class ArticleTag(Base):
    __tablename__ = "article_tags"

    article_id: Mapped[int] = mapped_column(
        ForeignKey("articles.id")
    )

    tag_id: Mapped[int] = mapped_column(
        ForeignKey("tags.id")
    )

    __table_args__ = (
        PrimaryKeyConstraint(
            "article_id",
            "tag_id"
        ),
    )