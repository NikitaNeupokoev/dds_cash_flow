from django.urls import path

from . import views
from .views import (
    CashFlowListView,
    CashFlowCreateView,
    CashFlowUpdateView,
    CashFlowDeleteView
)

app_name = 'cash_flow'

urlpatterns = [
    # Основные CRUD операции
    path(
        '',
        CashFlowListView.as_view(),
        name='record_list'
    ),
    path(
        'create/',
        CashFlowCreateView.as_view(),
        name='record_create'
    ),
    path(
        '<int:pk>/edit/',
        CashFlowUpdateView.as_view(),
        name='record_edit'
    ),
    path(
        '<int:pk>/delete/',
        CashFlowDeleteView.as_view(),
        name='record_delete'
    ),

    # Управление справочниками
    path(
        'references/',
        views.reference_management,
        name='reference_management'
    ),
]
