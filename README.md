# 📚 uchet_knig — Система учёта книг (CLI)

Консольное приложение для учёта домашней/библиотечной коллекции книг.  
Поддерживает добавление, просмотр, отметку прочтения и удаление записей.  
Данные хранятся в локальной SQLite-базе.

## 🛠 Стек технологий
- **Python 3.10+**
- `sqlite3` — встроенная реляционная БД
- `dataclasses` — типизированные модели данных
- `tabulate` — форматированный вывод в консоль
- `pytest` — модульное и интеграционное тестирование
- `flake8` — статический анализ кода (PEP 8)

## 📦 Установка
```bash
# Клонирование репозитория
git clone https://github.com/Svider-0/uchet_knig.git
cd uchet_knig

# Создание виртуального окружения
python -m venv venv
.\venv\Scripts\activate  # Windows

# Установка зависимостей
pip install -r requirements.txt

# Инициализация БД
python -m src.main init

# Добавление книги
python -m src.main add --title "1984" --author "Дж. Оруэлл" --year 1949 --isbn "978-0451524935" --read

# Просмотр всех книг
python -m src.main list

# Отметить как прочитанную
python -m src.main read 1

# Удалить книгу
python -m src.main delete 1

# Запуск тестов с подробным выводом
pytest tests/ -v

# Проверка стиля кода
flake8 src/ tests/ --max-line-length=100
