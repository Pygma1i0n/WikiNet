from app.database.database import SessionLocal
from sqlalchemy import inspect
from app.database.crud.user import (
    create_user,
    get_user,
    update_user,
    delete_user
)

from app.database.crud.article import (
    create_article,
    get_article,
    update_article,
    delete_article
)

from app.database.crud.comment import (
    create_comment,
    get_comment,
    update_comment,
    delete_comment
)

from app.database.crud.rating import (
    create_rating,
    get_rating,
    update_rating,
    delete_rating
)

from app.database.crud.tag import (
    create_tag,
    get_tag,
    update_tag,
    delete_tag
)


def main():
    db = SessionLocal()

    try:
        print("=== USER CRUD ===")

        user = create_user(
            db,
            username="test_user",
            email="test@example.com",
            password_hash="test_hash",
            role="READER"
        )
        print(inspect(user).persistent)
        print("CREATE:", user.id, user.username)

        print("READ:", user.id, user.username)

        user = update_user(
            db,
            user.id,
            username="updated_user"
        )
        print("UPDATE:", user.username)

        print("DELETE:", delete_user(db, user.id))


        print("\n=== ARTICLE CRUD ===")

        # Для статьи нужен пользователь-автор
        author = create_user(
            db,
            username="author",
            email="author@example.com",
            password_hash="hash",
            role="EDITOR"
        )

        article = create_article(
            db,
            title="Тестовая статья",
            article_type="LORE",
            author_id=author.id,
            description="Описание",
            content="Содержимое статьи"
        )
        print("CREATE:", article.id, article.title)

        article = get_article(db, article.id)
        print("READ:", article.id, article.title)

        article = update_article(
            db,
            article.id,
            title="Обновлённая статья"
        )
        print("UPDATE:", article.title)



        print("\n=== COMMENT CRUD ===")

        comment = create_comment(
            db,
            user_id=author.id,
            article_id=article.id,
            text="Тестовый комментарий"
        )
        print("CREATE:", comment.id)

        comment = get_comment(db, comment.id)
        print("READ:", comment.text)

        comment = update_comment(
            db,
            comment.id,
            "Изменённый комментарий"
        )
        print("UPDATE:", comment.text)

        print("DELETE:", delete_comment(db, comment.id))


        print("\n=== RATING CRUD ===")

        rating = create_rating(
            db,
            user_id=author.id,
            article_id=article.id,
            value=5
        )
        print("CREATE:", rating.id, rating.value)

        rating = get_rating(db, rating.id)
        print("READ:", rating.value)

        rating = update_rating(
            db,
            rating.id,
            4
        )
        print("UPDATE:", rating.value)

        print("DELETE:", delete_rating(db, rating.id))

        print("DELETE:", delete_article(db, article.id))
        print("DELETE:", delete_user(db,author.id))



        print("\n=== TAG CRUD ===")

        tag = create_tag(db, "test")
        print("CREATE:", tag.id, tag.name)

        tag = get_tag(db, tag.id)
        print("READ:", tag.name)

        tag = update_tag(
            db,
            tag.id,
            "updated"
        )
        print("UPDATE:", tag.name)

        print("DELETE:", delete_tag(db, tag.id))

    finally:
        db.close()


if __name__ == "__main__":
    main()