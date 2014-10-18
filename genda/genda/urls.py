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
    # Examples:
    # url(r'^$', 'genda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r"/login", LoginHandler),
    # url(r"/logout", LogoutHandler),
    # url(r"/test", TestHandler),
    # url(r"/users", UsersHandler),
    # url(r"/create_user", CreateUserHandler),
    # url(r"/everything", EverythingHandler)
    url(r'^demo/', demo),
    url(r'^api/', include(v1_api.urls)),
    url(r'^foundation', include(foundation.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^", index),
    url(r'^accounts/', include('nopassword.urls')),
    url(r'^profile/$', profile),
)
