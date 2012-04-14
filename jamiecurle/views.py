from django.core.urlresolvers import reverse
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    return render_to_response( 'home.html', {},
            context_instance=RequestContext(request))


def redirect_tags(request, tag):
    return HttpResponsePermanentRedirect(reverse('omblog:tag', args=[tag]))