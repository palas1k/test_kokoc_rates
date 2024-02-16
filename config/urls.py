from django.conf.urls import include, url
from django.contrib import admin

from src.rates.views import CurrencyView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', CurrencyView.as_view(), name='index'),
]
