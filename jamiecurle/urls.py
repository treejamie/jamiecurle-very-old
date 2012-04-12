from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponsePermanentRedirect
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('omblog.urls', namespace='omblog')),
    # redirect tags
    # TODO - redirect tags from /tags/$TAG to /blog/tags/$TAG
    # redirect blog.html - this can be removed once the SE's have caught up
    url(r'^blog.html$',
        lambda r: HttpResponsePermanentRedirect(reverse('omblog:index')),
        name='blog'),

    # finally the catch all
    url(r'^$', 'omblog.views.index', name='home')
)
