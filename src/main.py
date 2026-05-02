import argparse
import sys
from typing import Optional

from src.models import Book
from src.database import init_db
from src.repository import add_book, get_all_books, update_read_status, delete_book
from src.view import print_books_table


def parse_args(args: Optional[list[str]] = None) -> argparse.Namespace:
    """Парсит аргументы командной строки.

    Args:
        args: Список аргументов для тестирования.
              Если None, используется sys.argv[1:].

    Returns:
        argparse.Namespace: Объект с распознанными параметрами.
    """
    parser = argparse.ArgumentParser(description="📚 Система учёта книг (CLI)")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Доступные команды")

    subparsers.add_parser("init", help="Инициализировать базу данных")

    p_add = subparsers.add_parser("add", help="Добавить новую книгу")
    p_add.add_argument("--title", required=True, help="Название книги")
    p_add.add_argument("--author", required=True, help="Автор")
    p_add.add_argument("--year", type=int, required=True, help="Год издания")
    p_add.add_argument("--isbn", default="", help="ISBN (опционально)")
    p_add.add_argument("--read", action="store_true", help="Сразу отметить как прочитанную")

    subparsers.add_parser("list", help="Показать список всех книг")

    p_read = subparsers.add_parser("read", help="Отметить книгу как прочитанную")
    p_read.add_argument("id", type=int, help="ID книги")

    p_del = subparsers.add_parser("delete", help="Удалить книгу")
    p_del.add_argument("id", type=int, help="ID книги")

    return parser.parse_args(args)


def main() -> None:
    """Главная точка входа приложения."""
    args = parse_args()

    try:
        if args.command == "init":
            init_db()
            print("✅ База данных успешно инициализирована.")

        elif args.command == "add":
            book = Book(
                title=args.title,
                author=args.author,
                year=args.year,
                isbn=args.isbn,
                is_read=args.read,
            )
            new_id = add_book(book)
            print(f"📖 Книга добавлена. ID: {new_id}")

        elif args.command == "list":
            books = get_all_books()
            print_books_table(books)

        elif args.command == "read":
            if update_read_status(args.id, True):
                print(f"✅ Книга #{args.id} отмечена как прочитанная.")
            else:
                print(f"❌ Книга с ID {args.id} не найдена.")

        elif args.command == "delete":
            if delete_book(args.id):
                print(f"🗑️ Книга #{args.id} удалена.")
            else:
                print(f"❌ Книга с ID {args.id} не найдена.")

    except Exception as e:
        print(f"⚠️ Ошибка выполнения: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
