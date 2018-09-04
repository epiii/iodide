from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

import server.views


admin.autodiscover()

urlpatterns = [
    # user urls
    #url(r'^user/$', server.views.user, name='user'),
    url(r'^user/(?P<name>[a-zA-Z0-9]+)', server.views.user, name='user'),

    # notebook stuff
    url(r'^api/v1/', include('server.notebooks.api_urls')),
    url(r'^notebooks/', include('server.notebooks.urls')),
    url(r'^new/?', server.notebooks.views.new_notebook_view,
        name='new-notebook'),

    # various views to help with the authentication pipeline
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^login_success/$', server.views.login_success,
        name='login_success'),
    url(r'^logout/$', server.views.logout, name='logout'),
    url(r'^login/?', server.views.login, name='login'),

    # admin stuff
    path('admin/', admin.site.urls),
    url(r'^$', server.views.index, name='index'),
]
