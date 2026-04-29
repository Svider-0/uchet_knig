import os
import sqlite3
import pytest
from src.database import init_db, DB_PATH


@pytest.fixture(autouse=True)
def clean_db():
    """Удаляет тестовую БД до и после каждого теста."""
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    yield
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)


def test_init_db_creates_table():
    """Проверяет создание файла БД и таблицы books."""
    init_db()

    assert os.path.exists(DB_PATH), "Файл БД не был создан"

    conn = sqlite3.connect(DB_PATH)
    try:
        query = (
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name='books';"
        )
        cursor = conn.execute(query)
        assert cursor.fetchone() is not None, (
            "Таблица books не найдена в схеме"
        )
    finally:
        conn.close()
