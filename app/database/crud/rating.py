from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.rating import Rating


def create_rating(
    db: Session,
    user_id: int,
    article_id: int,
    value: int
) -> Rating:

    rating = Rating(
        user_id=user_id,
        article_id=article_id,
        value=value
    )

    db.add(rating)
    db.commit()
    db.refresh(rating)

    return rating


def get_rating(db: Session, rating_id: int) -> Rating | None:
    return db.get(Rating, rating_id)


def get_ratings(db: Session) -> list[Rating]:
    return db.scalars(select(Rating)).all()


def update_rating(
    db: Session,
    rating_id: int,
    value: int
) -> Rating | None:

    rating = db.get(Rating, rating_id)

    if rating is None:
        return None

    rating.value = value

    db.commit()
    db.refresh(rating)

    return rating


def delete_rating(db: Session, rating_id: int) -> bool:
    rating = db.get(Rating, rating_id)

    if rating is None:
        return False

    db.delete(rating)
    db.commit()

    return True