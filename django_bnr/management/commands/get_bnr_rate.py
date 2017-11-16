# -*- coding: utf-8 -*-
# vim: ft=python:sw=4:ts=4:sts=4:et:
import datetime
import decimal

from optparse import make_option

from django.core.management.base import BaseCommand
from django_bnr.utils import get_bnr_rate
from django_bnr.models import CURRENCIES


class Command(BaseCommand):
    help = 'Gets the BNR rate for given currency'

    def add_arguments(self, parser):
        parser.add_argument(
            "-c",
            "--currency",
            type=str,
            choices=CURRENCIES,
            dest="currency",
            action="store",
            default="USD",
            help="Currency to get rate for",
        )

        # Named (optional) arguments
        parser.add_argument(
            "-d",
            "--date",
            type=str,
            dest="date",
            action="store",
            default=datetime.date.today().strftime("%Y-%m-%d"),
            help="Date to get rate for",
        )

    def handle(self, *args, **options):
        currency = options['currency']
        date = datetime.datetime.strptime(options['date'], '%Y-%m-%d').date()
        print(get_bnr_rate(date, currency))
