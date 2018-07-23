"""
Definition of urls for stockmarket.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from stock  import views


import stock.forms
import stock.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', stock.views.home, name='home'),
    url(r'^stock/', views.StockList.as_view()),
    url(r'^contact$', stock.views.contact, name='contact'),
    url(r'^about', stock.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'stock/login.html',
            'authentication_form': stock.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns=format_suffix_patterns(urlpatterns)