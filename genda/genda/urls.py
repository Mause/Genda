from django.conf.urls import patterns, include, url
from django.contrib import admin

import foundation.urls
from genders.views import index, profile, demo

from genders.api import resolve_mapping

urlpatterns = patterns(
    '',
    url(r'^demo/', demo),
    url(r'^api/(?P<email_hash>[^/]*)/', resolve_mapping),
    url(r'^foundation', include(foundation.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('nopassword.urls')),
    url(r'^profile/$', profile),
    url(r"^$", index),
)
