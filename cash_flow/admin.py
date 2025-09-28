from django.contrib import admin

from .models import (
    CashFlow,
    Category,
    Status,
    Subcategory,
    Type
)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """Админка для статусов."""

    list_display = ['name']
    search_fields = ['name']
    list_per_page = 20


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    """Админка для типов операций."""

    list_display = ['name']
    search_fields = ['name']
    list_per_page = 20


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админка для категорий."""

    list_display = ['name', 'type']
    list_filter = ['type']
    search_fields = ['name']
    list_per_page = 20


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    """Админка для подкатегорий."""

    list_display = ['name', 'category']
    list_filter = ['category', 'category__type']
    search_fields = ['name']
    list_per_page = 20


@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    """Админка для денежных потоков."""

    list_display = [
        'operation_date',
        'status',
        'type',
        'category',
        'subcategory',
        'amount'
    ]
    list_filter = [
        'status',
        'type',
        'category',
        'operation_date'
    ]
    search_fields = ['description']
    date_hierarchy = 'operation_date'
    list_per_page = 50

    fieldsets = (
        ('Основная информация', {
            'fields': (
                'operation_date',
                'status',
                'type',
                'amount'
            )
        }),
        ('Классификация', {
            'fields': ('category', 'subcategory')
        }),
        ('Дополнительная информация', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
    )
