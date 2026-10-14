from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.tag import Tag


def create_tag(db: Session, name: str) -> Tag:
    tag = Tag(name=name)

    db.add(tag)
    db.commit()
    db.refresh(tag)

    return tag


def get_tag(db: Session, tag_id: int) -> Tag | None:
    return db.get(Tag, tag_id)


def get_tags(db: Session) -> list[Tag]:
    return db.scalars(select(Tag)).all()


def update_tag(
    db: Session,
    tag_id: int,
    name: str
) -> Tag | None:

    tag = db.get(Tag, tag_id)

    if tag is None:
        return None

    tag.name = name

    db.commit()
    db.refresh(tag)

    return tag


def delete_tag(db: Session, tag_id: int) -> bool:
    tag = db.get(Tag, tag_id)

    if tag is None:
        return False

    db.delete(tag)
    db.commit()

    return True