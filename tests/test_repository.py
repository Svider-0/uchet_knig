import pytest
from src.database import init_db
from src.models import Book
from src.repository import add_book, get_all_books, update_read_status, delete_book
from src.view import print_books_table


@pytest.fixture
def test_db(tmp_path):
    """Создаёт временную БД для каждого теста."""
    db_file = tmp_path / "test_books.db"
    init_db(str(db_file))
    return str(db_file)


def test_add_and_get_all_books(test_db):
    """Проверяет добавление и получение списка книг."""
    book = Book(title="1984", author="Дж. Оруэлл", year=1949, isbn="978-0451524935")
    new_id = add_book(book, test_db)
    assert new_id == 1

    books = get_all_books(test_db)
    assert len(books) == 1
    assert books[0].title == "1984"


def test_update_read_status(test_db):
    """Проверяет обновление статуса прочтения."""
    add_book(Book(title="Test", author="A", year=2020), test_db)
    assert update_read_status(1, True, test_db) is True

    book = get_all_books(test_db)[0]
    assert book.is_read is True


def test_delete_book(test_db):
    """Проверяет удаление книги."""
    add_book(Book(title="ToDelete", author="B", year=2021), test_db)
    assert delete_book(1, test_db) is True
    assert len(get_all_books(test_db)) == 0


def test_print_books_table(capsys, test_db):
    """Проверяет корректный вывод таблицы через tabulate."""
    add_book(Book(title="Python Crash Course", author="Eric Matthes", year=2019), test_db)
    books = get_all_books(test_db)
    print_books_table(books)

    captured = capsys.readouterr()
    assert "Python Crash Course" in captured.out
    assert "Eric Matthes" in captured.out
    assert "grid" not in captured.out  # Проверка, что выводится только таблица
