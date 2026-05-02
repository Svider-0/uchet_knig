import pytest
from src.main import parse_args


def test_parse_args_init():
    """Проверяет парсинг команды init."""
    args = parse_args(["init"])
    assert args.command == "init"


def test_parse_args_add():
    """Проверяет парсинг команды add с обязательными и опциональными флагами."""
    args = parse_args([
        "add",
        "--title", "1984",
        "--author", "Дж. Оруэлл",
        "--year", "1949",
        "--isbn", "978-0451524935",
        "--read",
    ])
    assert args.command == "add"
    assert args.title == "1984"
    assert args.author == "Дж. Оруэлл"
    assert args.year == 1949
    assert args.isbn == "978-0451524935"
    assert args.read is True


def test_parse_args_id_commands():
    """Проверяет парсинг команд, требующих ID."""
    read_args = parse_args(["read", "42"])
    assert read_args.command == "read"
    assert read_args.id == 42

    del_args = parse_args(["delete", "7"])
    assert del_args.command == "delete"
    assert del_args.id == 7


def test_parse_args_invalid(capsys):
    """Проверяет корректное завершение при неверной команде."""
    with pytest.raises(SystemExit):
        parse_args(["unknown_command"])
