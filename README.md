# DDS Cash Flow - Учет движения денежных средств

Веб-приложение для учета денежных операций с фильтрацией и управлением справочниками.

## Функциональность

- Создание, редактирование, удаление записей
- Фильтрация по дате, статусу, типу, категориям
- Управление справочниками (статусы, типы, категории)
- Валидация связей между данными

## Технологии

- Python 3.9+
- Django 4.2+
- SQLite
- Bootstrap 5

## Быстрый запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/NikitaNeupokoev/dds_cash_flow.git
cd dds_cash_flow

# 2. Создать виртуальное окружение
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Настроить БД
python manage.py migrate
python manage.py load_initial_data

# 5. Запустить сервер
python manage.py runserver
```

## Автор:  
_Неупокоев Никита_<br>
**email**: _n.neupokoev154@yandex.ru_<br>
**telegram** _@NikitaNeupokoev_<br>
**github** _https://github.com/NikitaNeupokoev_
