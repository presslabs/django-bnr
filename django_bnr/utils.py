# -*- coding: utf-8 -*-
# vim: ft=python:sw=4:ts=4:sts=4:et:
import requests
import decimal

from datetime import timedelta
from xml.etree import ElementTree

from django_bnr.models import Rate


def get_bnr_rate(date, currency='USD'):
    try:
        rate = Rate.objects.get(date=date, currency=currency)
        return rate.rate
    except Rate.DoesNotExist:
        d = date.strftime('%Y-%m-%d')
        r = requests.get('https://www.bnr.ro/nbrfxrates10days.xml')
        r.raise_for_status()
        rate = None
        days = 0
        xpath_fmt = ("./{xsd}Body/{xsd}Cube[@date='{date}']/"
                     "{xsd}Rate[@currency='{currency}']")
        while rate is None:
            rate = ElementTree.fromstring(r.text).find(xpath_fmt.format(
                xsd='{http://www.bnr.ro/xsd}',
                date=d,
                currency=currency
            ))
            if rate is None:
                days += 1
                if days == 7:
                    raise RuntimeError('Cannot get exchange rate for '
                                       '%(currency)s from %(date)s' % {
                                           'currency': currency,
                                           'date': date
                                       })
                d = (date - timedelta(days=days)).strftime('%Y-%m-%d')

        rate = decimal.Decimal(rate.text)
        try:
            Rate.objects.create(date=date, currency=currency, rate=rate)
        except:
            pass
        return rate
