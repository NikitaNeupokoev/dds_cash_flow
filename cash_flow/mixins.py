from .models import Category, Subcategory


class CashFlowFormMixin:
    """Миксин с общей логикой для форм CashFlow."""

    def get_context_data(self, **kwargs):
        """Добавляет категории и подкатегории в контекст шаблона."""
        context = super().get_context_data(**kwargs)
        context.update({
            'all_categories': Category.objects.all(),
            'all_subcategories': Subcategory.objects.all(),
        })
        return context

    def _validate_category_relationships(self, form):
        """
        Проверяет связи между типом, категорией и подкатегорией.

        Возвращает False если найдены несоответствия.
        """
        cleaned_data = form.cleaned_data
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')
        selected_type = cleaned_data.get('type')

        if category and category.type != selected_type:
            form.add_error(
                'category',
                'Категория не принадлежит выбранному типу'
            )
            return False

        if subcategory and subcategory.category != category:
            form.add_error(
                'subcategory',
                'Подкатегория не принадлежит выбранной категории'
            )
            return False

        return True
