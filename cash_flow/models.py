from django.db import models


class CashFlow(models.Model):
    date = models.DateField('Дата операции')
    amount = models.DecimalField(
        'Сумма',
        max_digits=10,
        decimal_places=2
    )
    description = models.CharField(
        'Описание',
        max_length=200
    )

    def __str__(self):
        return f'{self.date} - {self.amount} - {self.description}'
