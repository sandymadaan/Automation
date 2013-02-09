from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^$', direct_to_template,
                    { 'template': 'index.html' }, 'index'),
    (r'^hello', direct_to_template,
                    { 'template': 'job_ok.html' }, ),
    (r'^tcc11_12/', include('Automation.tcc.urls')),
    

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'', include('gmapi.urls.media')),
    (r'^accounts/', include('registration.urls')),
   
)

