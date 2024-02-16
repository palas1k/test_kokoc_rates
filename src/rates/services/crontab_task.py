# -*- coding: utf-8 -*-
from django.contrib.sites import requests

from src.rates.models import CurrencyRate


def get_currencies_rate(self, *args, **kwargs):
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    data = response.json()
    valute = {}
    for currency_code, rate in data['Valute'].items():
        valute[currency_code] = rate['Value']
    CurrencyRate.objects.create(currencies=valute)


get_currencies_rate()
