# -*- coding: utf-8 -*-
from collections import OrderedDict

from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from rates.models import CurrencyRate


class CurrencyView(DetailView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        charcode = request.GET.get('charcode')
        date = request.GET.get('date')
        currency = get_object_or_404(CurrencyRate, date=date)
        rate = currency.currencies.get(charcode, None)
        if rate is not None:
            response = OrderedDict([
                ("charcode", charcode),
                ("date", date),
                ("rate", rate)
            ])
            return JsonResponse(response)
        else:
            return HttpResponseNotFound("Валюта и ее курс не найдены на указанную дату")
