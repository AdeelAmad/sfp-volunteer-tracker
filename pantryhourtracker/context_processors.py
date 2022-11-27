from django.conf import settings
# Context processor for version number and site name
# Version
def version(request):
    return {'version': settings.VERSION_COPYRIGHT}

def site_name(request):
    return {'org_name': settings.SITE_NAME}