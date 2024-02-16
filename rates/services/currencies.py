# -*- coding: utf-8 -*-
import requests

from rates.models import CurrencyRate


class BaseManager:
    pass


class CurrenciesManager(BaseManager):
    """
        Метод для запроса текущего курса валют у ЦБ и записи их в бд
        :return None
    """

    def get_currencies_rate(self, *args, **kwargs):
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        data = response.json()
        valute = {}
        for currency_code, rate in data['Valute'].items():
            valute[currency_code] = rate['Value']
        CurrencyRate.objects.create(currencies=valute)


def update_currency_rate():
    manager = CurrenciesManager()
    manager.get_currencies_rate()

update_currency_rate()
