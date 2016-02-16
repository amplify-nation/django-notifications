# -*- coding: utf-8 -*-

from django.conf import urls
from .views import all, unread, mark_all_as_read, mark_as_read, mark_as_unread

urlpatterns = urls.patterns(
    '',
    urls.url(
        r'^',
        all,
        name='all'
    ),
    urls.url(
        r'^unread/$',
        unread,
        name='unread'
    ),
    urls.url(
        r'^mark-all-as-read/$',
        mark_all_as_read,
        name='mark_all_as_read'
    ),
    urls.url(
        r'^mark-as-read/(?P<slug>\d+)/$',
        mark_as_read,
        name='mark_as_read'
    ),
    urls.url(
        r'^mark-as-unread/(?P<slug>\d+)/$',
        mark_as_unread,
        name='mark_as_unread'
    ),
)
