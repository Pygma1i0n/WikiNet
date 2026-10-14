from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.user import User


def create_user(
    db: Session,
    username: str,
    email: str,
    password_hash: str,
    role: str = "READER"
) -> User:
    user = User(
        username=username,
        email=email,
        password_hash=password_hash,
        role=role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)


def get_users(db: Session) -> list[User]:
    return db.scalars(select(User)).all()


def update_user(
    db: Session,
    user_id: int,
    username: str | None = None,
    email: str | None = None,
    role: str | None = None,
    is_blocked: bool | None = None
) -> User | None:

    user = db.get(User, user_id)

    if user is None:
        return None

    if username is not None:
        user.username = username

    if email is not None:
        user.email = email

    if role is not None:
        user.role = role

    if is_blocked is not None:
        user.is_blocked = is_blocked

    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, user_id: int) -> bool:
    user = db.get(User, user_id)

    if user is None:
        return False

    db.delete(user)
    db.commit()

    return True