from django.template import RequestContext

def base_template(request):
    if not request.user.is_active:
        return {"base_template": "base_noclient.html"}
    if not request.user.is_staff:
        return {"base_template": "base_client.html"}
    return "base.html"
