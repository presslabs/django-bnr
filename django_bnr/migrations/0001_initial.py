# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.DecimalField(null=True, verbose_name=b'Exchange rate', max_digits=8, decimal_places=4, blank=True)),
                ('date', models.DateField(db_index=True)),
                ('currency', models.CharField(default=b'USD', max_length=3, db_index=True, choices=[(b'CHF', b'CHF'), (b'EUR', b'EUR'), (b'GBP', b'GBP'), (b'USD', b'USD')])),
            ],
            options={
                'ordering': ['-date', 'currency'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together=set([('date', 'currency')]),
        ),
    ]
