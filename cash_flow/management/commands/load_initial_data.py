from django.core.management.base import BaseCommand
from cash_flow.models import (
    Status,
    Type,
    Category,
    Subcategory
)
from cash_flow.constants import (
    INITIAL_STATUSES,
    INITIAL_TYPES,
    INITIAL_CATEGORIES
)


class Command(BaseCommand):
    help = 'Загрузка начальных данных для справочников'

    def handle(self, *args, **options):
        self.stdout.write('Начинаем загрузку начальных данных...')

        # Создаем статусы
        for status_name in INITIAL_STATUSES:
            status, created = Status.objects.get_or_create(
                name=status_name
            )
            if created:
                self.stdout.write(
                    f'✓ Создан статус: {status_name}'
                )

        # Создаем типы операций
        for type_name in INITIAL_TYPES:
            type_obj, created = Type.objects.get_or_create(
                name=type_name
            )
            if created:
                self.stdout.write(
                    f'✓ Создан тип операции: {type_name}'
                )

        # Создаем категории и подкатегории
        for category_data in INITIAL_CATEGORIES:
            type_obj = Type.objects.get(
                name=category_data['type']
            )
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                type=type_obj
            )
            if created:
                self.stdout.write(
                    f'✓ Создана категория:'
                    f'{category_data["name"]} ({type_obj})'
                )

            # Создаем подкатегории для категории
            for subcategory_name in category_data['subcategories']:
                subcategory, created = Subcategory.objects.get_or_create(
                    name=subcategory_name,
                    category=category
                )
                if created:
                    self.stdout.write(
                        f'  ✓ Создана подкатегория: {subcategory_name}'
                    )

        self.stdout.write('✅ Начальные данные успешно загружены!')
