from django.conf.urls import include, url
from django.contrib import admin

from rates.views import CurrencyView

urlpatterns = [
    # Examples:
    # url(r'^$', 'config.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', CurrencyView.as_view(), name='index'),
]
