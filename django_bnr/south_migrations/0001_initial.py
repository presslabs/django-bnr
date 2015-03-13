# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rate'
        db.create_table(u'django_bnr_rate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=4, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(db_index=True)),
            ('currency', self.gf('django.db.models.fields.CharField')(default='USD', max_length=3, db_index=True)),
        ))
        db.send_create_signal(u'django_bnr', ['Rate'])

        # Adding unique constraint on 'Rate', fields ['date', 'currency']
        db.create_unique(u'django_bnr_rate', ['date', 'currency'])


    def backwards(self, orm):
        # Removing unique constraint on 'Rate', fields ['date', 'currency']
        db.delete_unique(u'django_bnr_rate', ['date', 'currency'])

        # Deleting model 'Rate'
        db.delete_table(u'django_bnr_rate')


    models = {
        u'django_bnr.rate': {
            'Meta': {'ordering': "['-date', 'currency']", 'unique_together': "(('date', 'currency'),)", 'object_name': 'Rate'},
            'currency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '3', 'db_index': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '4', 'blank': 'True'})
        }
    }

    complete_apps = ['django_bnr']