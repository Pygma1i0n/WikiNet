from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.article import Article


def create_article(
    db: Session,
    title: str,
    article_type: str,
    author_id: int,
    description: str | None = None,
    content: str | None = None,
    publication_status: str = "DRAFT"
) -> Article:

    article = Article(
        title=title,
        type=article_type,
        author_id=author_id,
        description=description,
        content=content,
        publication_status=publication_status
    )

    db.add(article)
    db.commit()
    db.refresh(article)

    return article


def get_article(db: Session, article_id: int) -> Article | None:
    return db.get(Article, article_id)


def get_articles(db: Session) -> list[Article]:
    return db.scalars(select(Article)).all()


def update_article(
    db: Session,
    article_id: int,
    title: str | None = None,
    description: str | None = None,
    content: str | None = None,
    publication_status: str | None = None
) -> Article | None:

    article = db.get(Article, article_id)

    if article is None:
        return None

    if title is not None:
        article.title = title

    if description is not None:
        article.description = description

    if content is not None:
        article.content = content

    if publication_status is not None:
        article.publication_status = publication_status

    db.commit()
    db.refresh(article)

    return article


def delete_article(db: Session, article_id: int) -> bool:
    article = db.get(Article, article_id)

    if article is None:
        return False

    db.delete(article)
    db.commit()

    return True