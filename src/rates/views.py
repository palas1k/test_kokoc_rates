# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views.generic import DetailView
from src.rates.services.currencies import CurrenciesManager


class CurrencyView(DetailView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        manager = CurrenciesManager()
        response = manager.get_rate_from_db(request)
        return JsonResponse(response)
