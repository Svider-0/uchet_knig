import sqlite3
import os
from typing import Optional


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(PROJECT_ROOT, "data", "books.db")


def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    """Возвращает подключение к SQLite базе данных.

    Args:
        db_path: Путь к файлу БД. Если None, используется DB_PATH.

    Returns:
        sqlite3.Connection: Объект подключения с row_factory=sqlite3.Row.
    """
    path = db_path or DB_PATH
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: Optional[str] = None) -> None:
    """Создаёт таблицу `books`, если она ещё не существует.

    Args:
        db_path: Путь к файлу БД для тестирования.
    """
    conn = get_connection(db_path)
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL,
                isbn TEXT UNIQUE,
                is_read BOOLEAN DEFAULT 0
            )
        """)
        conn.commit()
    finally:
        conn.close()
