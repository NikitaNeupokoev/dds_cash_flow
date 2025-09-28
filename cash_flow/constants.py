# Бизнес-константы
MAX_NAME_LENGTH = 100
MAX_DESCRIPTION_LENGTH = 200
AMOUNT_MAX_DIGITS = 12
AMOUNT_DECIMAL_PLACES = 2

# Начальные данные
INITIAL_STATUSES = ['Бизнес', 'Личное', 'Налог']
INITIAL_TYPES = ['Пополнение', 'Списание']

# Примеры категорий и подкатегорий из ТЗ
INITIAL_CATEGORIES = [
    {
        'name': 'Инфраструктура',
        'type': 'Списание',
        'subcategories': ['VPS', 'Proxy']
    },
    {
        'name': 'Маркетинг',
        'type': 'Списание',
        'subcategories': ['Farpost', 'Avito']
    },
    {
        'name': 'Зарплата',
        'type': 'Пополнение',
        'subcategories': ['Аванс', 'Основная часть']
    }
]
