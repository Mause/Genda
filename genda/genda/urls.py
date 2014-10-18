from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

import foundation.urls
from genders.views import index

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
    url(r'^foundation', include(foundation.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^", index),
)
