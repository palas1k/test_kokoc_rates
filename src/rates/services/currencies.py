# -*- coding: utf-8 -*-

from collections import OrderedDict

from django.core.exceptions import SuspiciousOperation, FieldDoesNotExist, ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from src.rates.models import CurrencyRate


class BaseManager:
    pass


class CurrenciesManager(BaseManager):
    @staticmethod
    def __check_charcode_and_date(charcode, date):
        if charcode is None or date is None:
            raise SuspiciousOperation("Не указан тикер или дата")


    @staticmethod
    def __get_currency_from_db(rate):
        if rate is None:
            raise ObjectDoesNotExist("Валюты с таким тикером не существует")

    def get_rate_from_db(self, request):
        charcode = request.GET.get('charcode')
        date = request.GET.get('date')
        self.__check_charcode_and_date(charcode=charcode, date=date)
        try:
            currency = get_object_or_404(CurrencyRate, date=date)
        except Exception:
            raise FieldDoesNotExist("В базе не содержится курса валют на указанную дату")
        rate = currency.currencies.get(charcode, None)
        self.__get_currency_from_db(rate)
        data = OrderedDict([
            ("charcode", charcode),
            ("date", date),
            ("rate", rate)
        ])
        return data
