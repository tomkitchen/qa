from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^flashcards/', include('flashcards.urls')),
    url(r'^module308/', include('module308.urls')),
    url(r'^module316/', include('module316.urls')),
    url(r'^module307/', include('module307.urls')),
    url(r'^module309/', include('module309.urls')),
    url(r'^module310/', include('module310.urls')),
    url(r'^module312/', include('module312.urls')),
    url(r'^module315/', include('module315.urls')),
    url(r'^ccnp/', include('ccnp.urls')),
    url(r'^osce/', include('osce.urls')),
    url(r'^$', include('homepage.urls'))
)
