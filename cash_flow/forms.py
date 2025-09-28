from django import forms

from .models import (
    CashFlow,
    Category,
    Status,
    Subcategory,
    Type
)


class CashFlowRecordForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = [
            'operation_date',
            'status',
            'type',
            'category',
            'subcategory',
            'amount',
            'description'
        ]
        widgets = {
            'operation_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'required': True
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'subcategory': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0.01',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Необязательный комментарий...'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Простая инициализация - все категории и подкатегории доступны
        # Валидация будет на уровне модели


class CashFlowFilterForm(forms.Form):
    """Форма для фильтрации записей"""

    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        label='С даты'
    )

    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        label='По дату'
    )

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='Статус'
    )

    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='Тип операции'
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='Категория'
    )

    subcategory = forms.ModelChoiceField(
        queryset=Subcategory.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='Подкатегория'
    )
