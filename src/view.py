from tabulate import tabulate
from .models import Book


def print_books_table(books: list[Book]) -> None:
    """Выводит список книг в консоль в виде таблицы.

    Args:
        books: Список объектов Book для отображения.
    """
    if not books:
        print("📚 Список книг пуст.")
        return

    table_data = [
        (b.id, b.title, b.author, b.year, b.isbn or "—", "✅" if b.is_read else "❌")
        for b in books
    ]
    headers = ["ID", "Название", "Автор", "Год", "ISBN", "Прочитано"]
    print(tabulate(table_data, headers, tablefmt="grid"))
