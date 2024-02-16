from django.db import models
from django_mysql.models import JSONField


class CurrencyRate(models.Model):
    date = models.DateField(auto_now=True)
    currencies = JSONField(default=dict)

    def __str__(self):
        return str(self.date)
