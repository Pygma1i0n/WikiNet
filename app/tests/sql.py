from sqlalchemy import select

from app.database.database import SessionLocal
from app.database.models.article import Article
from app.database.models.tag import Tag
from app.database.models.article_tag import ArticleTag


session = SessionLocal()

try:
    stmt = (
        select(Tag)
        .join(ArticleTag, Tag.id == ArticleTag.tag_id)
        .join(Article, Article.id == ArticleTag.article_id)
        .where(Article.author_id == 12)
        .distinct()
    )

    tags = session.execute(stmt).scalars().all()


finally:
    session.close()






for tag in tags:
    print(f"- {tag.name}")