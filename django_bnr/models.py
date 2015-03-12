from django.db import models

CURRENCIES = ('USD', 'EUR', 'CHF', 'GBP')


class Rate(models.Model):
    rate = models.DecimalField(max_digits=8, decimal_places=4, null=True,
                               blank=True, verbose_name=('Exchange rate'))
    date = models.DateField(db_index=True)
    currency = models.CharField(choices=((c, c) for c in sorted(CURRENCIES)),
                                max_length=3, db_index=True, default='USD')

    class Meta:
        ordering = ['-date', 'currency']
        unique_together = ('date', 'currency')
