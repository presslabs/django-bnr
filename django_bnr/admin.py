from django.contrib import admin
from django_bnr.models import Rate


# Register your models here.
class RateAdmin(admin.ModelAdmin):
    list_display = ('rate', 'currency', 'date')


admin.site.register(Rate, RateAdmin)
