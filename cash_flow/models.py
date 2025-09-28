from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from .constants import (
    AMOUNT_DECIMAL_PLACES,
    AMOUNT_MAX_DIGITS,
    MAX_NAME_LENGTH,
)


class Status(models.Model):
    """Статусы записей: Бизнес, Личное, Налог."""

    name = models.CharField(
        'Название статуса',
        max_length=MAX_NAME_LENGTH,
        unique=True
    )

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Type(models.Model):
    """Типы операций: доходы и расходы."""

    name = models.CharField(
        'Название типа',
        max_length=MAX_NAME_LENGTH,
        unique=True
    )

    class Meta:
        verbose_name = 'Тип операции'
        verbose_name_plural = 'Типы операций'

    def __str__(self):
        return self.name


class Category(models.Model):
    """Категории операций, привязанные к типам"""

    name = models.CharField(
        'Название категории',
        max_length=MAX_NAME_LENGTH,
        help_text='Например: Инфраструктура, Маркетинг'
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        verbose_name='Тип операции',
        related_name='categories'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['type', 'name']
        unique_together = ['name', 'type']

    def __str__(self):
        return f"{self.name} ({self.type})"


class Subcategory(models.Model):
    """Подкатегории, привязанные к категориям"""

    name = models.CharField(
        'Название подкатегории',
        max_length=MAX_NAME_LENGTH,
        help_text='Например: VPS, Proxy, Farpost'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='subcategories'
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['category', 'name']
        unique_together = ['name', 'category']

    def __str__(self):
        return f"{self.name} ({self.category})"


class CashFlow(models.Model):
    """Основная модель для записей ДДС"""

    created_at = models.DateTimeField(
        'Дата и время создания записи',
        auto_now_add=True
    )

    operation_date = models.DateField(
        'Дата операции',
        help_text='Выберите дату, когда была совершена операция'
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name='Статус операции'
    )

    type = models.ForeignKey(
        Type,
        on_delete=models.PROTECT,
        verbose_name='Тип операции'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='Категория',
        blank=True,
        null=True
    )

    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.PROTECT,
        verbose_name='Подкатегория',
        blank=True,
        null=True
    )

    amount = models.DecimalField(
        'Сумма',
        max_digits=AMOUNT_MAX_DIGITS,
        decimal_places=AMOUNT_DECIMAL_PLACES,
        validators=[MinValueValidator(0.01)],
        help_text='Сумма в рублях'
    )

    description = models.TextField(
        'Описание операции',
        blank=True,
        help_text='Необязательное поле для комментариев'
    )

    class Meta:
        verbose_name = 'Запись ДДС'
        verbose_name_plural = 'Записи ДДС'
        ordering = ['-operation_date', '-created_at']

    def clean(self):
        """Валидация связей между полями"""
        super().clean()

        # Проверяем что категория принадлежит выбранному типу
        if self.category and self.category.type != self.type:
            raise ValidationError({
                'category': f'Категория "{self.category}"'
                f'не принадлежит типу "{self.type}"'
            })

        # Проверяем что подкатегория принадлежит выбранной категории
        if self.subcategory and self.subcategory.category != self.category:
            raise ValidationError({
                'subcategory': f'Подкатегория "{self.subcategory}"'
                f'не принадлежит категории "{self.category}"'
            })

    def __str__(self):
        return (
            f'{self.operation_date} - {self.type} - {self.amount} руб.'
        )
