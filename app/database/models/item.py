from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Item(Base):
    __tablename__ = "items"

    article_id: Mapped[int] = mapped_column(
        ForeignKey("articles.id"),
        primary_key=True
    )

    item_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )