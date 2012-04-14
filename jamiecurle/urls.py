from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponsePermanentRedirect
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/',
            include(admin.site.urls)),
    url(r'^about.html',
            'django.views.generic.simple.direct_to_template',
            {'template': 'about.html'},
            name='about'),
    url(r'^blog/',
            include('omblog.urls',
            namespace='omblog')),
    url(r'^404/',
            'django.views.generic.simple.direct_to_template',
            {'template': '404.html'},
            name='404'),
    url(r'^500/',
            'django.views.generic.simple.direct_to_template',
            {'template': '500.html'},
            name='404'),

    url(r'^503/',
            'django.views.generic.simple.direct_to_template',
            {'template': '503.html'},
            name='503'),
    # redirects - can be removed once the SE's have caught up
    #
    #
    url(r'^tags/(?P<tag>[\w]+)$',
            'jamiecurle.views.redirect_tags'),    
    url(r'^blog.html$',
            lambda r: HttpResponsePermanentRedirect(reverse('omblog:index')),
            name='blog'),

    # finally the catch all
    url(r'^$',
            'omblog.views.index',
            name='home')
)

