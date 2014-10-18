from django.conf.urls import patterns, include, url
from django.contrib import admin

import foundation.urls
from genders.views import index, profile, demo

from tastypie.api import Api
from genders.api import AllPronounsResource

v1_api = Api(api_name='v1')
v1_api.register(AllPronounsResource())

urlpatterns = patterns(
    '',
    url(r'^demo/', demo),
    url(r'^api/', include(v1_api.urls)),
    url(r'^foundation', include(foundation.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('nopassword.urls')),
    url(r'^profile/$', profile),
    url(r"^$", index),
)
