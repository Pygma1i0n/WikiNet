from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.comment import Comment


def create_comment(
    db: Session,
    user_id: int,
    article_id: int,
    text: str
) -> Comment:

    comment = Comment(
        user_id=user_id,
        article_id=article_id,
        text=text
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment


def get_comment(db: Session, comment_id: int) -> Comment | None:
    return db.get(Comment, comment_id)


def get_comments(db: Session) -> list[Comment]:
    return db.scalars(select(Comment)).all()


def update_comment(
    db: Session,
    comment_id: int,
    text: str
) -> Comment | None:

    comment = db.get(Comment, comment_id)

    if comment is None:
        return None

    comment.text = text

    db.commit()
    db.refresh(comment)

    return comment


def delete_comment(db: Session, comment_id: int) -> bool:
    comment = db.get(Comment, comment_id)

    if comment is None:
        return False

    db.delete(comment)
    db.commit()

    return True