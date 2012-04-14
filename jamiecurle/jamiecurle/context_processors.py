

def disqus_developer(request):
    from django.conf import settings
    return{
        'DISQUS_DEVELOPER': getattr(settings, 'DISQUS_DEVELOPER', False)
    }