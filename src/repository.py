from typing import Optional

from .models import Book
from .database import get_connection


def add_book(book: Book, db_path: Optional[str] = None) -> int:
    """Добавляет книгу в БД и возвращает её сгенерированный ID.

    Args:
        book: Объект модели Book с заполненными полями.
        db_path: Путь к тестовой БД.

    Returns:
        int: ID новой записи.
    """
    conn = get_connection(db_path)
    try:
        cursor = conn.execute(
            "INSERT INTO books (title, author, year, isbn, is_read) "
            "VALUES (?, ?, ?, ?, ?)",
            (book.title, book.author, book.year, book.isbn, book.is_read),
        )
        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()


def get_all_books(db_path: Optional[str] = None) -> list[Book]:
    """Возвращает список всех книг из таблицы.

    Args:
        db_path: Путь к тестовой БД.

    Returns:
        list[Book]: Список объектов Book.
    """
    conn = get_connection(db_path)
    try:
        rows = conn.execute(
            "SELECT id, title, author, year, isbn, is_read FROM books"
        ).fetchall()
        books = []
        for row in rows:
            data = dict(row)
            # SQLite возвращает 0/1 вместо bool, приводим явно
            data["is_read"] = bool(data["is_read"])
            books.append(Book(**data))
        return books
    finally:
        conn.close()


def update_read_status(
    book_id: int, is_read: bool, db_path: Optional[str] = None
) -> bool:
    """Изменяет статус прочтения книги по ID.

    Args:
        book_id: ID книги.
        is_read: Новый статус.
        db_path: Путь к тестовой БД.

    Returns:
        bool: True, если запись найдена и обновлена.
    """
    conn = get_connection(db_path)
    try:
        cursor = conn.execute(
            "UPDATE books SET is_read = ? WHERE id = ?",
            (is_read, book_id),
        )
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()


def delete_book(book_id: int, db_path: Optional[str] = None) -> bool:
    """Удаляет книгу по ID.

    Args:
        book_id: ID книги.
        db_path: Путь к тестовой БД.

    Returns:
        bool: True, если запись найдена и удалена.
    """
    conn = get_connection(db_path)
    try:
        cursor = conn.execute(
            "DELETE FROM books WHERE id = ?", (book_id,)
        )
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()
