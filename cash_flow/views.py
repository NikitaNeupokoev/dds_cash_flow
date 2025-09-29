from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView
)
from django.urls import reverse_lazy
from django.contrib import messages

from .models import (
    CashFlow,
    Category,
    Status,
    Subcategory,
    Type
)
from .forms import (
    CashFlowFilterForm,
    CashFlowRecordForm
)
from .mixins import CashFlowFormMixin
from .constants import VIEW_PAGINATE_BY


class CashFlowListView(ListView):
    """Список записей CashFlow с пагинацией и фильтрацией."""

    model = CashFlow
    template_name = 'cash_flow/record_list.html'
    paginate_by = VIEW_PAGINATE_BY
    context_object_name = 'records'

    def get_queryset(self):
        """
        Возвращает отфильтрованный queryset
        по форме из GET-параметров.
        """
        queryset = super().get_queryset()
        self.filter_form = CashFlowFilterForm(self.request.GET)

        if self.filter_form.is_valid():
            cleaned_data = self.filter_form.cleaned_data

            date_from = cleaned_data.get('date_from')
            date_to = cleaned_data.get('date_to')

            if date_from:
                queryset = queryset.filter(
                    operation_date__gte=date_from
                )
            if date_to:
                queryset = queryset.filter(
                    operation_date__lte=date_to
                )

            if cleaned_data.get('status'):
                queryset = queryset.filter(
                    status=cleaned_data['status']
                )
            if cleaned_data.get('type'):
                queryset = queryset.filter(
                    type=cleaned_data['type']
                )
            if cleaned_data.get('category'):
                queryset = queryset.filter(
                    category=cleaned_data['category']
                )
            if cleaned_data.get('subcategory'):
                queryset = queryset.filter(
                    subcategory=cleaned_data['subcategory']
                )

        return queryset

    def get_context_data(self, **kwargs):
        """
        Добавляет в контекст форму фильтра
        и дополнительные данные.
        """
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.filter_form
        context['total_amount'] = sum(
            record.amount for record in context['records']
        )

        context.update({
            'all_statuses': Status.objects.all(),
            'all_types': Type.objects.all(),
            'all_categories': Category.objects.all(),
            'all_subcategories': Subcategory.objects.all(),
        })

        return context


class CashFlowCreateView(CashFlowFormMixin, CreateView):
    """Создание новой записи о движении денежных средств."""

    model = CashFlow
    form_class = CashFlowRecordForm
    template_name = 'cash_flow/record_form.html'
    success_url = reverse_lazy('cash_flow:record_list')

    def form_valid(self, form):
        """Сохраняет запись после успешной валидации связей."""
        if not self._validate_category_relationships(form):
            return self.form_invalid(form)

        messages.success(self.request, 'Запись успешно создана!')
        return super().form_valid(form)


class CashFlowUpdateView(CashFlowFormMixin, UpdateView):
    """Редактирование существующей записи о движении денежных средств."""

    model = CashFlow
    form_class = CashFlowRecordForm
    template_name = 'cash_flow/record_form.html'
    success_url = reverse_lazy('cash_flow:record_list')

    def form_valid(self, form):
        """Сохраняет изменения после успешной валидации связей."""
        if not self._validate_category_relationships(form):
            return self.form_invalid(form)

        messages.success(self.request, 'Запись успешно обновлена!')
        return super().form_valid(form)


class CashFlowDeleteView(DeleteView):
    model = CashFlow
    template_name = 'cash_flow/record_confirm_delete.html'
    success_url = reverse_lazy('cash_flow:record_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Запись успешно удалена!')
        return super().delete(request, *args, **kwargs)


def reference_management(request):
    """Страница управления справочниками"""
    context = {
        'statuses': Status.objects.all(),
        'types': Type.objects.all(),
        'categories': Category.objects.all(),
        'subcategories': Subcategory.objects.all(),
    }
    return render(
        request,
        'cash_flow/reference_management.html',
        context
    )
