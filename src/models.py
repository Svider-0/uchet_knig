from dataclasses import dataclass
from typing import Optional


@dataclass
class Book:
    """Модель книги для системы учёта.

    Attributes:
        id: Уникальный идентификатор (генерируется БД).
        title: Название книги.
        author: Автор книги.
        year: Год издания.
        isbn: Международный стандартный книжный номер.
        is_read: Статус прочтения (по умолчанию False).
    """
    id: Optional[int] = None
    title: str = ""
    author: str = ""
    year: int = 0
    isbn: str = ""
    is_read: bool = False
