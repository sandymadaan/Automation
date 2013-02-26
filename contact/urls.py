from Auto.contact.forms import *
from django.conf.urls.defaults import *

urlpatterns = patterns("Auto.contact.views",
    (r"^contact(\d+)/$", "contact"),
)

